from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_p, name = 'account'),
    path('login/', views.login_p, name = 'login'),
    path('signup/', views.signup_p, name = 'signup'),
    path('reset_pass/', views.reset_pass_p, name = 'reset_pass'),
]