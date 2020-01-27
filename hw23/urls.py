from django.urls import path
# from .views import api_car, api_car_detail
from .views import APICar, APICarDetail


urlpatterns = [
    path('car/', APICar.as_view(), name='APICar_url'),
    path('car/<int:pk>', APICarDetail.as_view()),
]
