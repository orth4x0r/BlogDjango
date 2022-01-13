
from collections import UserList, UserString
from django import forms
import django
from django.contrib.auth import base_user, get_user, get_user_model
from django.contrib.auth.models import User
from django.db import models
import datetime
from django.http import request
from django.shortcuts import render



class NewPost(forms.Form):
    titulo = forms.CharField(required=True)
    fecha = forms.DateField(initial=datetime.date.today)
    texto = forms.CharField(required=True)
    autor = forms.CharField(initial="")
    imagen = forms.ImageField(required=False)



