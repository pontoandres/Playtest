from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.views.generic import ListView
from .models import Game
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
  

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class GameListView(ListView):
    model = Game
    template_name = 'game_list.html'  # El template donde se muestran los juegos
    context_object_name = 'games'

    def get_queryset(self):
        # Mostrar todos los juegos para todos los usuarios
        return Game.objects.all()
    
class UploadGameView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Game
    fields = ['title', 'file']
    template_name = 'upload_game.html'
    success_url = '/'

    def test_func(self):
        return self.request.user.groups.filter(name='Developers').exists()

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