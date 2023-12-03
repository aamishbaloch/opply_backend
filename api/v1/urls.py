from django.urls import include, path
from api.v1.authentication import urls as auth_urls

urlpatterns = [
    path('auth/', include(auth_urls)),
]
