from django.shortcuts import render
from .models import Empolye
from .forms import EmpForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request,'home.html')

def get_empolye(request):
    emp=Empolye.objects.all()
    return render(request,'view.html',{'emp':emp})

@login_required
def add_empolye(request):
    if (request.POST):
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return get_empolye(request)
    else:
        form=EmpForm()
    return render(request,'add.html',{'form':form})

@login_required
def update_employe(request,pk):
    e=Empolye.objects.get(id=pk)
    if(request.POST):
        form=EmpForm(request.POST,instance=e)
        if form.is_valid():
            form.save()
            return get_empolye(request)
    else:
        form=EmpForm(instance=e)
    return render(request,'add.html',{'form':form})

@login_required
def delete(request,pk):
    e=Empolye.objects.get(id=pk)
    e.delete()
    return home(request)

def register(request):
    if request.POST:
        username=request.POST['username']
        email = request.POST['email']
        password=request.POST['password']
        cp = request.POST['cp']

        if(password == cp):
            u=User.objects.create_user(username=username,email=email,password=password)
            u.save()
            return user_login(request)
        else:
            return  HttpResponse("password are not same")
    return render(request,'register.html')

def user_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse("invalid password or username")
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)




