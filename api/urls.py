from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import UserDetailView

schema_view = get_schema_view(
    openapi.Info(
        title="Quebrei API",
        default_version='v1',
        description="Documentação da API para o Quebrei",
        contact=openapi.Contact(email="suporte@exemplo.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Swagger
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Auth
urlpatterns += [
    path('auth/', UserDetailView.as_view(), name='login'),
    path('auth/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
]
