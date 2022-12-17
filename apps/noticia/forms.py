from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña", required=True, widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username","email","password1","password2","first_name","last_name"]
        help_texts = { k:"" for k in fields }