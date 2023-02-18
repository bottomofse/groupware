from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'