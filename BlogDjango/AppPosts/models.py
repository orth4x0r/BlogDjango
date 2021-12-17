from django.db import models

# Create your models here.

class User(models.Model):
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Post(models.Model):
    imagen = models.ImageField()
    titulo = models.CharField(max_length=50)
    fecha = models.DateField()
    texto = models.CharField(max_length=1000)

class Intro(models.Model):
    bienvenida = models.CharField(max_length=50)
    nosotrxs = models.CharField(max_length=1000)
    foto = models.ImageField()