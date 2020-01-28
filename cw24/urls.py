from django.urls import path
from .views import index, Image, SaveImage, SendMessage

urlpatterns = [
    path('', index, name='index_url'),
    path('image/', Image.as_view(), name='image_url'),
    path('image/save', SaveImage.as_view(), name='save_url'),
    path('message/', SendMessage.as_view(), name='message_url'),
]
