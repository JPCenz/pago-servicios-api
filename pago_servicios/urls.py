"""pago_servicios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from api_pagos.v1.router import api_urlpatterns as api_v1
from api_pagos.v2.router import api_urlpatterns as api_v2

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from users.urls import  urlpatterns

# Vista general e información de la API
schema_view = get_schema_view(
    openapi.Info(
        title="API Pagos de Servicios Streaming",
        default_version="v2",
        description="Proyecto final ",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^api/v1/', include((api_v1,"api"),namespace='v1')),
    re_path(r'^api/v2/', include((api_v2,"api"),namespace='v2',),),
]

