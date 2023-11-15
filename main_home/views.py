from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, 'home/index.html')
def menu(request):
    return render(request, 'home/other/menu.html')
def logout_p(request):
    logout(request)
    return redirect('home')
def cart(request): 
    return redirect('../users/')