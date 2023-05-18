from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def signup_p(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        
        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()
        
        # Redirect to login page or any other desired page
        return redirect('login')
    
    return render(request, 'users/other/signup.html')
def account_p(request):
    return render(request, 'users/account.html')
def login_p(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Login user
            login(request, user)
            
            # Redirect to the desired page
            return redirect('home')
        else:
            error_message = "Invalid email or password."
            return render(request, 'users/other/login.html', {'error_message': error_message})
    
    return render(request, 'users/other/login.html')
def reset_pass_p(request):
    return render(request, 'users/other/resetpass.html')

