from django.shortcuts import render
from django.views import View

# https://docs.djangoproject.com/en/5.0/topics/auth/default/
class LandingPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class LoginPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

class DashboardView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard.html')
