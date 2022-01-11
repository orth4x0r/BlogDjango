from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('verPost', args=(str(self.id)))

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_tag = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
#    cuerpoPost = models.TextField()
    cuerpoPost = RichTextField(blank=True, null=True)
    fechaPost = models.DateField(auto_now_add=True)
    categoria_post = models.CharField(max_length=255, default="misc")

    def __str__(self):
        return self.titulo +' | ' + str(self.autor)
    
    def get_absolute_url(self):
        return reverse('verPost', args=(str(self.id)))
