from django.urls import path
from .views import *

urlpatterns = [
    path('home/customer/', cw21, name='cw21_url'),
    path('home/', home, name='home_url'),
]