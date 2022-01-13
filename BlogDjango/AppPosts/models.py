from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"usuario: {self.usuario}, password: {self.password}"

class Post(models.Model):
    imagen = models.ImageField()
    titulo = models.CharField(max_length=50)
    fecha = models.DateField(default=date.today)
    texto = models.CharField(max_length=1000)
    autor = models.CharField(max_length=50)

    def __str__(self):
        return f"titulo: {self.titulo}, fecha: {self.fecha}, autor: {self.autor}"

class Intro(models.Model):
    bienvenida = models.CharField(max_length=50)
    nosotrxs = models.CharField(max_length=1000)
    foto = models.ImageField()

    def __str__(self):
        return f"bienvenida: {self.bienvenida}, nosotrxs: {self.nosotrxs}, foto: {self.foto}"