from django.urls import path
from .views import api_car

urlpatterns = [
    path('car/', api_car)
]
