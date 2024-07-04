from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SecionForm(forms.Form):
    usuario = forms.CharField(max_length=150, label='Nombre de Usuario')
    contraseña = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

class RegistrarceForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Repetir contraseña',
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise ValidationError("Este campo es obligatorio.")
        if not all(char.isalnum() or char in "@.+-_" for char in username):
            raise ValidationError("Ingrese un nombre de usuario válido. Este valor puede contener solo letras, números y @/./+/-/_ caracteres.")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        if username and password1 and username.lower() in password1.lower():
            raise ValidationError("La contraseña es demasiado similar al nombre de usuario.")
        return password2
