from django.shortcuts import render
from.models import Autor, Categoria, Livro, Emprestimo, Aluno, Curso

def home(request):
    
    return render(request, 'home.html')

def alunos(request):
    alunos = Aluno.objects.all
    return render(request, 'alunos.html',{'alunos':alunos})

def emprestimos(request):
    emprestimos = Emprestimo.objects.all
    alunos = Aluno.objects.all
    return render(request, 'emprestimos.html',{'emprestimos':emprestimos , 'alunos':alunos})

def livros(request):
    livros = Livro.objects.all
    return render(request, 'livros.html',{'livros':livros})
