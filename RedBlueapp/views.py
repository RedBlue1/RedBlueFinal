from django.shortcuts import render,HttpResponse
import pandas as pd

# Create your views here.
def index(request):
    return render(request, "index.html")
def SignUp(request):
    return render(request, "User/auth-sign-up.html")
def SignIn(request):
    return render(request, "User/auth-sign-in.html")
def RecoverPw(request):
    return render(request, "User/auth-recoverpw.html")