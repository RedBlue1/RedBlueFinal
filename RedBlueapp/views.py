from django.shortcuts import render,HttpResponse
from .models import nifty_50

# Create your views here.
def index(request):
    data = nifty_50.objects.all()
    return render(request, "index.html",{"nifty": data})
def SignUp(request):
    return render(request, "User/auth-sign-up.html")
def SignIn(request):
    return render(request, "User/auth-sign-in.html")
def RecoverPw(request):
    return render(request, "User/auth-recoverpw.html")
def user_after_login(request):
    data = nifty_50.objects.all()
    return render(request, "User/user_after_login.html", {"nifty": data})
