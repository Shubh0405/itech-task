from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'api/index.html',{})

def signup(request):
    registered = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True

        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request,'api/signup.html',{'form':form,'registered':registered})

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email,password=password)

        if user:
            if user.is_active:
                auth_login(request,user)
                return HttpResponseRedirect(reverse('api:home'))

            else:
                return HttpResponse("Account not active")

        else:
            print("Invalid details")
            return redirect('login')

    else:
        return render(request,'api/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('api:home'))

def cal_func(x,n):

    sum = 0
    for i in range(1,n+1):
        sum += (1/(x)**i)

    return sum

def cal_func_using_recrusion(x,n):

    if n==1:
        return 1/x
    else:
        return 1/(x**n) + cal_func_using_recrusion(x,n-1)

@login_required
def display_result(request):
    ans = None
    if request.method == "POST":
        x = request.POST.get("x")
        n = request.POST.get("n")

        ans = cal_func_using_recrusion(int(x),int(n))


    return render(request,'api/calculate.html',{'ans':ans})
