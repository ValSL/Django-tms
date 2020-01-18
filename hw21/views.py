from django.shortcuts import render, reverse
from .models import User
from .forms import UserForm
from django.shortcuts import redirect


def user_list(request):
    users = User.objects.all()
    return render(request, 'hw21/user_list.html', context={'users': users})


def user_detail(request, id):
    user = User.objects.get(id=id)
    return render(request, 'hw21/user_detail.html', context={'user': user})


def user_create(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'hw21/user_create.html', context={'form': form})

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            return redirect('user_detail_url', id=new_user.id)
        return render(request, 'hw21/user_create.html', context={'form': form})


def user_edit(request, id):
    if request.method == 'GET':
        user = User.objects.get(id=id)
        form = UserForm(instance=user)
        return render(request, 'hw21/user_edit.html', context={'form': form, 'user': user})
    if request.method == 'POST':
        user = User.objects.get(id=id)
        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            updated_user = form.save()
            return redirect('user_detail_url', id=updated_user.id)
        return render(request, 'hw21/user_edit.html', context={'form': form, 'user': user})


def user_delete(request, id):
    if request.method == 'GET':
        user = User.objects.get(id=id)
        return render(request, 'hw21/user_delete.html', context={'user': user})

    if request.method == 'POST':
        User.objects.get(id=id).delete()
        return redirect('user_list_url')
