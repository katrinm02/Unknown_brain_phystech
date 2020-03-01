"""ks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from rest_framework.schemas import get_schema_view

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions
# 
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Blog API",
#       default_version='v1',
#       description="Test description",
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )
schema_view = get_schema_view(
    title='Server Monitoring API',
    url='https://localhost/pool/poolservices/'
)

urlpatterns = [
    path('admin/', admin.site.urls),
#     path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('pool/', include('pool.urls')),
    path('openapi/', schema_view, name='openapi-schema'),
]
