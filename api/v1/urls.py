from django.urls import include, path
from api.v1.authentication import urls as auth_urls
from api.v1.product import urls as product_urls
from api.v1.order import urls as order_urls

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('products/', include(product_urls)),
    path('orders/', include(order_urls)),
]
