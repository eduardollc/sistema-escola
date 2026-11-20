from django.db import models

# Create your models here.
class Aluno(models.Model):
    matricula = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100,)
    cpf = models.CharField(max_length=11, unique=True)
    idade = models.IntegerField()
    email= models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
