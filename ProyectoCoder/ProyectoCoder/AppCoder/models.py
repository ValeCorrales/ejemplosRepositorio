from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

# Create your models here.

#en python poniamos class Curso():

class Avatar(models.Model):
    
    #models.ForeignKey significa que estoy relacionando una clase de modelos con otra
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) #aca estoy relacionado la clase Avatar (que es 
    #nueva) con el modelo User, que es una clase de modelo de Django, por eso la tengo que importar- HAY 
    # UN AVATAR QUE ESTOY RELACIONANDO CON EL USUARIO. ON DELETE CASCADE
    #TIENE QUE VER CON COMANDOS DE BASE DE DATOS, COMO FUNCIONA EL ELIMINAR EN CASO DE ELIMINAR UN
    #USUARIO O UN AVATAR, BASICAMENTE SI ELIMNIMO UNO, ELIMNIMO EL OTRO
    
    #EL AVATAR a demas de tener una relacion con el usuario, tiene una imagen (tipo imagen):
    
    imagen = models.ImageField(upload_to='avatares', null = True, blank=True) #upload_to='avatares' es el 
    #directorio donde se va a subir, el cual se llama avatares, y despues ponemos que puede ser nulo y 
    # puede quedar en blanco

class Curso(models.Model): #este es nuestro primer modelo
    
    #aca tenemos que poner el tipo de datos de curso: models.VARIOSTIPOSDEDATOS = field - char: coleccion caracteres
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    esNoche = models.BooleanField(null=True)

    def __str__(self) -> str:
        return f"CURSO {self.nombre}, CAMADA: {self.camada}, NOCHE: {self.esNoche}"
    
class Jugador(models.Model):
    
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField(null=True)
    esBueno = models.BooleanField()
    
    def __str__(self) -> str:
        return f"{self.apellido}, {self.numero}, {self.esBueno}"
    
class Equipo(models.Model):
    
    nombre = models.CharField(max_length=40, null=True)
    ciudad = models.CharField(max_length=40, null=True)
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.ciudad}"
    
class Estadio(models.Model):
    
    direccion = models.CharField(max_length=40)
    anioFund = models.IntegerField()
    
    
class Empleado(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    profesional = models.BooleanField() #es un booleano, lo tildas o no lo tildas
    fechaDeNacimiento = models.DateField()
    
    def __str__(self) -> str:
        return f"NOMBRE: {self.nombre}, APELLIDO: {self.apellido},DNI: {self.dni}"
