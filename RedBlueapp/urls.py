from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('SignIn', views.SignIn, name='SignIn'),
    path('RecoverPw', views.RecoverPw, name='RecoverPw'),
    path('UserAfterLogin',views.user_after_login, name='UserAfterLogIn')
]
