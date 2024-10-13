from  django.contrib.auth.models import Group
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import Game
from .forms import GameUploadForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.contrib.auth import login
from django.views.generic import DetailView, ListView, DeleteView


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('game_list')  # Redirigir a la página de inicio después del registro

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Iniciar sesión automáticamente después del registro
        
        # Asignar el grupo "Testers" al usuario
        try:
            group = Group.objects.get(name='Testers')
            user.groups.add(group)
        except Group.DoesNotExist:
            messages.error(self.request, 'El grupo "Testers" no existe.')
            return redirect('register')
        
        # Agregar mensaje de éxito
        messages.success(self.request, 'Registro exitoso. Bienvenido a PlayTest!')
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, 'Error en el formulario. Por favor, corrige los errores.')
        return self.render_to_response(self.get_context_data(form=form))

class GameListView(ListView):
    model = Game
    template_name = 'game_list.html'  # El template donde se muestran los juegos
    context_object_name = 'games'

    def get_queryset(self):
        # Mostrar todos los juegos para todos los usuarios
        return Game.objects.all()
    
class UploadGameView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Game
    form_class = GameUploadForm
    template_name = 'upload_game.html'
    success_url = reverse_lazy('game_list')

    def test_func(self):
        return self.request.user.groups.filter(name='Developers').exists()

    def form_valid(self, form):
        game = form.save(commit=False)
        game.uploaded_by = self.request.user
        game.save()
        return super().form_valid(form)

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

class GameProfileView(DetailView):
    model = Game
    template_name = 'game_profile.html'
    context_object_name = 'game'

class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Game
    template_name = 'game_confirm_delete.html'
    success_url = reverse_lazy('game_list')

    def test_func(self):
        game = self.get_object()
        return self.request.user == game.uploaded_by