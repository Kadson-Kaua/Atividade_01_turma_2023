from django.db import models

# Create your models here.
class categoria(models.Model):
    nome = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome

class cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class filme(models.Model):
    titulo = models.CharField(max_length=150)
    valor = models.FloatField()
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
class locacao(models.Model):
    nome = models.CharField(max_length=150)
    data = models.DateField()
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    filme = models.ManyToManyField(filme)
    
    def __srt__(self):
        return self.nome


