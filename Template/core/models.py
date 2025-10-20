from django.db import models
from django.contrib.auth.models import AbstractUser

class Conta(models.Model):
    nome = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name="usuarios")
    telefone = models.CharField(max_length=20, blank=True)
