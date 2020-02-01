from django.urls import path
from .views import index, Image, SaveImage, SendMessage, animal_urls

urlpatterns = [
    path('', index, name='index_url'),
    path('image/', Image.as_view(), name='image_url'),
    path('image/save', SaveImage.as_view(), name='save_url'),
    path('message/', SendMessage.as_view(), name='message_url'),
    path('animals/', animal_urls, name='animal_url'),
]
