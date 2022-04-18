from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AutorFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)

class EditorialFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    web = forms.CharField(max_length=40)
    pais_origen = forms.CharField(max_length=40)

class LibrosFormulario(forms.Form):
    isbn = forms.IntegerField()
    idioma = forms.CharField(max_length=40)
    titulo = forms.CharField(max_length=100)
    fecha_publicacion = forms.DateField()
    clasificacion = forms.CharField(max_length=40)

class RegistroUsuarios(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Constraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username','email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}

class EditarUsuarios(UserCreationForm):

    email = forms.EmailField(label='Modificar Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Constraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}



        #python -m pip install Pillow