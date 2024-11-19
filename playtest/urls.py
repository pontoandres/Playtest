from django.contrib import admin
from django.urls import include, path
from myapp import views
from myapp.views import AddCommentView, DeleteCommentView, UploadGameView, UserProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('catalogo/', views.GameListView.as_view(), name='game_list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('tester/home/', views.TesterHomeView.as_view(), name='tester_home'),
    path('developer/home/', views.DeveloperHomeView.as_view(), name='developer_home'),
    path('developer/upload/', views.UploadGameView.as_view(), name='upload_game'),
    path('', views.HomePageView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('upload_game/', views.UploadGameView.as_view(), name='upload_game'),
    path('game/<int:pk>/', views.GameProfileView.as_view(), name='game_profile'),
    path('game/<int:pk>/delete/', views.GameDeleteView.as_view(), name='game_delete'),
    path('game/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('comment/<int:pk>/delete/', views.DeleteCommentView.as_view(), name='delete_comment'),
    path('game/<int:game_id>/details/', views.game_details, name='game_details'),

]