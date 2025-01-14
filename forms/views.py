from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your registration in Successful")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in Successfully")
            return redirect("dashboard")
            
        else:
            return render(request, "login.html", {"error": "Invalid email or password"})
    return render(request, "login.html")

@login_required(login_url="login")
def dashboard(request):
    messages.success(request, "You are now logged out Successfully")
    return render(request, "dashboard.html", {"user": request.user})
        

def user_logout(request):
    logout(request)
    return redirect("login")



