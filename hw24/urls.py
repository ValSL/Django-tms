from django.urls import path
from .views import index, ImageView, ImageSaveView, SendView


urlpatterns = [
    path('', index, name='hw24_index_url'),
    path('image/', ImageView.as_view(), name='random_image_url'),
    path('image/save/', ImageSaveView.as_view(), name='hw24_image_save_url'),
    path('image/send/', SendView.as_view(), name='hw24_send_url'),

]
