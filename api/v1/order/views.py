from django.db import transaction
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.serializers import OrderSerializer, OrderDetailSerializer
from entities.order.models import Order, OrderItem


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order_items = []
        for item in serializer.validated_data['items']:
            # TODO: This logic can be moved to order helper kind of a class to clear this view and
            #  also we can add this logic to order item manager so that items knows if they can be created or not
            required_product = item['product']
            required_quantity = item['quantity']

            if not required_product.sell_if_available(required_quantity):
                raise ValidationError({required_product.name: 'Number of required items not available'})

            order_items.append(OrderItem.objects.create(**item))

        order = Order.objects.create(customer_id=self.request.user.id)

        for order_item in order_items:
            order.items.add(order_item)

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class OrderHistoryAPIView(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Order.objects.filter(customer_id=self.request.user.id)
