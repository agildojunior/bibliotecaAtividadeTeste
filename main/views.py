from django.shortcuts import render
from .forms import LivroForm
from.models import Autor, Categoria, Livro, Emprestimo, Aluno, Curso

def home(request):
    
    return render(request, 'home.html')

def alunos(request):
    alunos = Aluno.objects.all
    return render(request, 'alunos.html',{'alunos':alunos})

def cadastrolivro(request):
    form = LivroForm()
    return render(request, "cadastrolivro.html", {'form':form})

def emprestimos(request):
    emprestimos = Emprestimo.objects.all
    alunos = Aluno.objects.all
    return render(request, 'emprestimos.html',{'emprestimos':emprestimos , 'alunos':alunos})

def livros(request):
    livros = Livro.objects.all
    return render(request, 'livros.html',{'livros':livros})

# def LivroForm(request):
#     form = LivroForm()
#     return render(request, "cadastrolivro.html", {'form':form})