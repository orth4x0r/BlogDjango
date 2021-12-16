
from django.urls import path
from .views import UserRegView
urlpatterns = [
    path('register/newuser', UserRegView.as_view(), name='register'),
]
