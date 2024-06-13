
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)  # nuevo campo
