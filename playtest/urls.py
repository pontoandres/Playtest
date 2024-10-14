from django.contrib import admin
from django.urls import include, path
from myapp import views
from myapp.views import AddCommentView, DeleteCommentView, UploadGameView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('tester/home/', views.TesterHomeView.as_view(), name='tester_home'), # Página de inicio para testers
    path('developer/home/', views.DeveloperHomeView.as_view(), name='developer_home'),# Página de inicio para Devs
    path('developer/upload/', views.UploadGameView.as_view(), name='upload_game'), # Página de subida de juegos
    path('', views.GameListView.as_view(), name='game_list'),  # Página de lista de juegos y HOME PAGE
    path('accounts/', include('django.contrib.auth.urls')),  
    path('accounts/logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('upload_game/', UploadGameView.as_view(), name='upload_game'), # Página de subida de juegos
    path('game/<int:pk>/', views.GameProfileView.as_view(), name='game_profile'),  # Página de perfil de juego
    path('game/<int:pk>/delete/', views.GameDeleteView.as_view(), name='game_delete'),  # Página de eliminación de juegos
    path('game/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),

]