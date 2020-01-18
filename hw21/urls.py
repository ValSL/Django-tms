from django.urls import path
from .views import *

urlpatterns = [
    path('', user_list, name='user_list_url'),
    path('user/<int:id>', user_detail, name='user_detail_url'),
    path('user/<int:id>/edit', user_edit, name='user_edit_url'),
]