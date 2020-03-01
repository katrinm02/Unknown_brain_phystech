from django.urls import path
from .views import ResultPoolServiceView
from . import views

app_name = 'pool_2'
urlpatterns = [
    path('resultpoolservices/', ResultPoolServiceView.as_view()),
    path('', views.home, name='home'),
#     path('poolservices/<path:pk>', PoolServiceView.as_view()),
]