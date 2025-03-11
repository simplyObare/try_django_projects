from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import RegisterUserForm
from resume.models import Resume
from company.models import Company


# register applicant only
def register_applicant(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.success(request, "Your account has been created successfully")
            return redirect("login")
        else:
            messages.error(request, "Registration failed")
            return redirect("register_applicant")
    else:
        form = RegisterUserForm()
        return render(request, "users/register_applicant.html", {"form": form})


# register recruiter only
def register_recruiter(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.success(request, "Your account has been created successfully")
            return redirect("login")
        else:
            messages.error(request, "Registration failed")
            return redirect("register_recruiter")
    else:
        form = RegisterUserForm()
        return render(request, "users/register_recruiter.html", {"form": form})


# login user
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    return render(request, "users/login.html")


# logout user
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("login")
