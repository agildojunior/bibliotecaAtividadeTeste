from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('alunos', views.alunos, name='alunos'),
    path('cadastrolivro', views.cadastrolivro, name='cadastrolivro'),
    path('emprestimos', views.emprestimos, name='emprestimos'),
    path('livros', views.livros, name='livros'),
    ]