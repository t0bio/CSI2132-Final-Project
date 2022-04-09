from django.shortcuts import render, redirect
from .forms import CreateAccountForm
# Create your views here.

def createAccount(response):
    if response.method =="POST":
        form = CreateAccountForm(response.POST)

        if form.is_valid():
            form.save()

        return redirect('receptionist')
    else:
        form = CreateAccountForm()
    
    return render(response, "authentication/createaccount.html", {"form":form})