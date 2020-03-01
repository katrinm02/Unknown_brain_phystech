from django.urls import path
from .views import PoolServiceView


app_name = 'pool'
urlpatterns = [
    path('poolservices/', PoolServiceView.as_view()),
]