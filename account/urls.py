from django.urls import path
from .views import *

urlpatterns = [
    path('create-user/', create_user, name='create_user'),
    path('login-user/', login_user, name='login_user'),
    path('update-user/', update_user, name='update_user'),
    path('log-out-user/', logout_user, name='logout_user'),
]