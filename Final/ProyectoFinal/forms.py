from django import forms
from django.forms import fields
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class AgregarForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class RegistroForm(UserCreationForm):

    
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password1",
            "password2",
        ]
        labels = {
            "email": "Correo Electronico",
            "username": "Nombre de usuario",
            "password1": "Contraseña",
            "password2": "Repetir contraseña",
        }