import datetime
from django import forms
import django

from django.contrib.auth.forms import UserCreationForm

class AvatarFormulario(forms.Form):

    #Especificar los campos

    imagen = forms.ImageField(required=True) 

class UserRegisterForm(UserCreationForm):
    
    #Obligatorios
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

   #Extra
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)
    
#meta: indicaciones que se sacan en esta linea que no sean atributos del usuario, de esta forma se ve mas limpio
#creas una clase meta

class EstadioFormulario(forms.Form):
    
    #especificar campos
    direccion = forms.CharField()
    anioFund = forms.IntegerField()
    
class EmpleadoFormulario(forms.Form):
    
    #los atributos de esta clase se pueden llamar como quieran, pero lo aconsejable
    #es que se llamen igual que el modelo, lo copiamos de ahi y cambiamos models por forms
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    profesional = forms.BooleanField() #es un booleano, lo tildas o no lo tildas
    fechaDeNacimiento = forms.DateField(initial=datetime.date.today)
    
    
class JugadorFormulario(forms.Form):
    
    #pego de models lo mismo, lo modifico por forms
    
    apellido = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    esBueno = forms.BooleanField()