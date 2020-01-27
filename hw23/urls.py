from django.urls import path
from .views import api_car, api_car_detail


urlpatterns = [
    path('car/', api_car, name='api_car_url'),
    path('car/<int:pk>', api_car_detail),
]
