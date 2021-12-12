from django.db import models

# Create your models here.

#en python poniamos class Curso():

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
    
class Equipo(models.Model):
    
    nombre = models.CharField(max_length=40, null=True)
    ciudad = models.CharField(max_length=40, null=True)
    
class Estadio(models.Model):
    
    direccion = models.CharField(max_length=40)
    anioFund = models.IntegerField()
