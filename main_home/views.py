from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')
def menu(request):
    return render(request, 'home/other/menu.html')