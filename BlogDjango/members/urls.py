
from django.urls import path
from .views import PasswordsChangeView, UserEditView, UserRegView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/newuser', UserRegView.as_view(), name='register'),
    path('edit_profile/newuser', UserEditView.as_view(), name='edit_profile'),
#    path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success', views.password_success, name="password_success")
]
