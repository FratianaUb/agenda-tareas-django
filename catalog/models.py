from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tarea(models.Model):
    Nombre = models.CharField(max_length=80)
    Descripción = models.TextField(blank=True)
    Creado = models.DateTimeField(auto_now_add=True)
    Fecha_completada =models.DateTimeField(null=True, blank=True)
    Importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Nombre + " - de " + self.user.username
       