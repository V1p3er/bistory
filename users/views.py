from django.shortcuts import render

def signup_p(request):
    return render(request, 'users/other/signup.html')
def account_p(request):
    return render(request, 'users/account.html')
def login_p(request):
    return render(request, 'users/other/login.html')
def reset_pass_p(request):
    return render(request, 'users/other/resetpass.html')
