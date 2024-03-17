from django.shortcuts import render, redirect
from main.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse


def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        User.objects.create_user(username=username, password=password, phone_number=phone_number)
        return redirect('index_url')
    return render(request, 'index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('index_url')
    return render(request, 'login.html')


def user_detail(request):
    context = {
        'user': request.user
    }
    return render(request, 'user-detail.html', context)


def update_user(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        img = request.FILES.get('img')
        username = request.POST.get('username')
        bio = request.POST.get('bio')
        phone_number = request.POST.get('phone_number')
        user.username = username
        user.bio = bio
        user.phone_number = phone_number
        user.img = img
        user.save()
        return HttpResponse("Home object created successfully!")

    return redirect('#')


def logout_user(request):
    logout(request)
    return redirect('login_url')
