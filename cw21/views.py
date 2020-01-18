from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Customer
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, 'cw21/home.html')


def cw21(request):
    if request.method == 'GET':
        form = CustomerForm()
        return render(request, 'cw21/add_customer.html', context={'form': form})

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_customer = Customer.objects.create(firstname=form.cleaned_data['firstname'],
                                                   lastname=form.cleaned_data['lastname'],
                                                   age=form.cleaned_data['age'],
                                                   profession=form.cleaned_data['profession'], )
            new_customer.save()
            return redirect('home_url')
        return render(request, 'cw21/add_customer.html', context={'form': form})
