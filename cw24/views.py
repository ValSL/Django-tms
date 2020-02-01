from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
import requests
from django.views import View
from .models import AnimalImage
from .forms import Message, FindForm
from django.db.models import Q


def index(request):
    form = FindForm()
    return render(request, 'cw24/cw24_index.html', context={'form': form})


class Image(View):
    def post(self, request):
        button = request.POST['button']
        if button == 'I love cats!':
            data = requests.get('https://aws.random.cat/meow').json()
            url = data['file']
            species = 'Cat'

        if button == 'I love dogs!':
            data = requests.get('https://dog.ceo/api/breeds/image/random').json()
            url = data['message']
            species = 'Dog'

        extension = url.split('.')[-1]

        animal = dict(url=url,
                      species=species,
                      type=extension, )
        request.session['animal'] = animal
        return render(request, 'cw24/cat.html', context={'url': url})

    def get(self, request):
        pass


class SaveImage(View):
    def post(self, request):
        if 'animal' in request.session:
            animal = request.session.get('animal')
            AnimalImage.objects.create(
                url=animal['url'],
                species=animal['species'],
                type=animal['type'],
            )
        return redirect('index_url')


class SendMessage(View):
    def get(self, request):
        form = Message()
        return render(request, 'cw24/message.html', context={'form': form})

    def post(self, request):
        form = Message(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data.get('subject'),
                form.cleaned_data.get('message'),
                form.cleaned_data.get('from_field'),
                [form.cleaned_data.get('to_field')],
                fail_silently=False,
            )
        return redirect('index_url')


def animal_urls(request):
    form = FindForm(request.POST)
    animals = []
    if form.is_valid():
        data = form.cleaned_data
        if data['animal'] == '1':
            animals = AnimalImage.objects.filter(species='Dog', type=data['image_type'])
        elif data['animal'] == '2':
            animals = AnimalImage.objects.filter(species='Cat', type=data['image_type'])
        return render(request, 'cw24/animal_url_list.html', context={'animals': animals})
