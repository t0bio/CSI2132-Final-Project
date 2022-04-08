from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def createAccount(response):
    if response.method =="POST":
        form = UserCreationForm(response.POST)

        if form.is_valid():
            form.save()

        return redirect('receptionist')
    else:
        form = UserCreationForm()
    
    return render(response, "authentication/createaccount.html", {"form":form})