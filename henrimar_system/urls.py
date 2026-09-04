
from django.contrib import admin
from django.urls import path
from app_cad_rotas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home.html"),
    path('rotas/', views.rota, name='listagem_rotas')
]
