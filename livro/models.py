from django.db import models
from django.utils import timezone
class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(default=timezone.now)
    emprestado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Livro'
