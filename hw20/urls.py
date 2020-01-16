from django.urls import path
from .views import *

urlpatterns = [
    path('', hw20, name='hw20_url')
]