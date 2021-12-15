from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_tag = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpoPost = models.TextField()

    def __str__(self):
        return self.titulo +' | ' + str(self.autor)
    
    def get_absolute_url(self):
        return reverse('verPost', args=(str(self.id)))