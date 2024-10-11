from django.contrib import admin
from django.urls import include, path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('tester/home/', views.TesterHomeView.as_view(), name='tester_home'),
    path('developer/home/', views.DeveloperHomeView.as_view(), name='developer_home'),
]