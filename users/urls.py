from django.urls import path
from . import views
from users.views import reset_pass_p, reset_password_confirm


urlpatterns = [
    path('', views.account_p, name = 'account'),
    path('login/', views.login_p, name = 'login'),
    path('signup/', views.signup_p, name = 'signup'),
    path('reset_pass/', views.reset_pass_p, name = 'reset_pass'),
    path('users/reset/<uidb64>/<token>/', reset_password_confirm, name='reset_password_confirm'),
]