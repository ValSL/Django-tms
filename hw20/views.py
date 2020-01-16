from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm


def hw20(request):
    if request.method == 'GET':
        form = OrderForm()
        return render(request, 'hw20/hw20.html', context={'form': form})
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if data.get('count_of_people')==1:
                return HttpResponse('<h1> Стоимость $100</h1>')
            else:
                return HttpResponse(f'<h1> Стоимость ${data.get("count_of_people") * 2 * 100}</h1>')
        return render(request, 'hw20/hw20.html', context={'form': form})
