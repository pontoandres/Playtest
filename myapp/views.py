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
from django.contrib.auth.views import LogoutView
  

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        # Asignar el grupo "Testers" al usuario
        try:
            group = Group.objects.get(name='Testers')
            user.groups.add(group)
        except Group.DoesNotExist:
            messages.error(self.request, 'El grupo "Testers" no existe.')
            return redirect('register')
        
        # Agregar mensaje de éxito
        messages.success(self.request, 'Registro exitoso. Bienvenido a PlayTest!')
        
        return response

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
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('game_list')