from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormRegistro(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Nombre de usuario requerido.')
    email = forms.EmailField(max_length=254, help_text='Correo electronico requerido.')

    class Meta:
        model = User
        fields = ('username','email','password1','password2',)
