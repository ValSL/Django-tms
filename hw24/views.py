from django.shortcuts import render, redirect
from .forms import ImageForm
from django.views import View
import requests
from random import randint
from .models import NatureImage
from django.core.mail import send_mail


def index(request):
    form = ImageForm()
    return render(request, 'hw24/index.html', context={'form': form})


class ImageView(View):
    def post(self, request):
        button = request.POST['button']
        form = ImageForm(request.POST)
        if form.is_valid():
            widht = form.cleaned_data['width']
            height = form.cleaned_data['height']
            rand = randint(1, 1000)
            data = requests.get(f'https://picsum.photos/id/{rand}/info').json()
            image = f'https://i.picsum.photos/id/{rand}/{widht}/{height}.jpg'
            request.session['data'] = data
            return render(request, 'hw24/image.html', context={'url': image})

    def get(self, request):
        pass


class ImageSaveView(View):
    def post(self, request):
        if 'data' in request.session:
            data = request.session['data']
            NatureImage.objects.create(
                url=data['download_url'],
                width=data['width'],
                height=data['height'],
                comment=request.POST['comment']
            )
        return render(request, 'hw24/send.html')


class SendView(View):
    def post(self, request):
        send_mail('Image', request.session['data']['download_url'], 'ValSLTest@yandex.by', ['ValSLTest@yandex.by'],
                  fail_silently=False)
        return redirect('hw24_index_url')
