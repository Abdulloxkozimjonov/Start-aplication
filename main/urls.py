from django.urls import path
from .views import *
from account.views import create_user

urlpatterns = [
    path('index/', index_view, name='index_url'),
    path('create/', create_user, name='create_ad_url'),
    path('single_ad/<int:pk>/', single_add, name='single_ad_url')
]
