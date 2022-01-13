from django.db import models

# Create your models here.

class User(models.Model):
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"usuario: {self.usuario}, password: {self.password}"

class Post(models.Model):
    imagen = models.ImageField()
    titulo = models.CharField(max_length=50)
    fecha = models.DateField()
    texto = models.CharField(max_length=1000)

    def __str__(self):
        return f"imagen: {self.imagen}, titulo: {self.titulo}, fecha: {self.fecha}"

class Intro(models.Model):
    bienvenida = models.CharField(max_length=50)
    nosotrxs = models.CharField(max_length=1000)
    foto = models.ImageField()

    def __str__(self):
        return f"bienvenida: {self.bienvenida}, nosotrxs: {self.nosotrxs}, foto: {self.foto}"