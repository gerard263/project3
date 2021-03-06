from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    if not request.user_is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "orders/index.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials"})
        
def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def register(request):
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    user = User.objects.create_user(username, email, password)
    user.first_name = firstname
    user.last_name = lastname
    user.save()