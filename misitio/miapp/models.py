from datetime import datetime
from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email de usuario')
    area = models.CharField(max_length=50)

    def __str__(self):
        return (self.nombre+' '+self.apellido)
    