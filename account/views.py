from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
import time
from django.contrib.auth.models import User
from .models import name


def home(request):
    return render(request,'home.html')
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request,'signup.html',context)
def welcome(request):
    return render(request,'welcome.html')
def logout(request):
    return render(request, 'logout.html')


