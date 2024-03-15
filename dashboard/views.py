from django.shortcuts import render
from main.models import User


def login_user(request):
    return render(request,'login.html',)


def register_user(request):
    return render(request, 'reg.html')