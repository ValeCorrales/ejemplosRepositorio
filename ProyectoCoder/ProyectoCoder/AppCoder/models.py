from django.db import models

# Create your models here.

#en python poniamos class Curso():

class Curso(models.Model): #este es nuestro primer modelo
    
    #aca tenemos que poner el tipo de datos de curso: models.VARIOSTIPOSDEDATOS = field - char: coleccion caracteres
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
class Jugador(models.Model):
    
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    esBueno = models.BooleanField()
