from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
import smtplib
import ssl



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
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request)
            reset_link = f"{current_site}/users/reset/{uid}/{token}/"
            subject = 'Reset Your Password'
            message = render_to_string('users/other/reset_email.html', {
                'user': user,
                'reset_link': reset_link,
                'current_site': current_site,
            })
            
            # Email sending configuration
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login('your_email@example.com', 'your_password')
            smtp_server.sendmail('your_email@example.com', [email], message)
            smtp_server.close()
            
            return render(request, 'users/')
        except User.DoesNotExist:
            return render(request, 'users/other/resetpass.html', {'error_message': 'Invalid email address.'})
    return render(request, 'users/other/resetpass.html')

def reset_password_confirm(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            if request.method == 'POST':
                password = request.POST['password']
                user.set_password(password)
                user.save()
                return render(request, 'reset_success.html')
            return render(request, 'users/other/reset_confirm.html')
    except (User.DoesNotExist, ValueError, OverflowError):
        pass
    return redirect('password_reset_failed')
