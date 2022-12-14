from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.CharField(max_length=3)

    def __str__(self):
        return str(self.nome)


class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    
    def __str__(self):
        return str(self.nome)


class Livro(models.Model):
    nome = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(str(self.nome))


class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return str(self.nome)


class Curso(models.Model):
    nome = models.CharField(max_length=200)
    aluno = models.ManyToManyField(Aluno, null=True, blank=True)

    def __str__(self):
        return str(self.nome)


class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True, blank=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True, blank=True)
