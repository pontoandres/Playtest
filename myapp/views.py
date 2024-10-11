from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")     

class RegisterView(View):
    def get(self, request):
        return HttpResponse("Register Page")
  

class TesterHomeView(UserPassesTestMixin, View):
    def test_func(self):
        # Permitir solo si el usuario es tester
        return self.request.user.is_tester

    def handle_no_permission(self):
        # Si el usuario no es un tester, redirigir a la página de inicio
        return redirect('home')

    def get(self, request):
        # Respuesta para los usuarios que tienen permiso (testers)
        return HttpResponse("Bienvenido Tester")
    
class DeveloperHomeView(UserPassesTestMixin, View):
    def test_func(self):
        # Permitir solo si el usuario es developer
        return self.request.user.is_developer

    def handle_no_permission(self):
        # Si el usuario no es un developer, redirigir a la página de inicio
        return redirect('home')

    def get(self, request):
        # Respuesta para los usuarios que tienen permiso (developers)
        return HttpResponse("Bienvenido Developer")