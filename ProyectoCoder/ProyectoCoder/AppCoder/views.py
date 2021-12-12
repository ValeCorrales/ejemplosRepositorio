from django.shortcuts import render

from django.http import HttpResponse
from AppCoder.forms import EstadioFormulario

from AppCoder.models import Equipo, Estadio 


# Create your views here.

def buscar(request):
    
    if request.GET["nombre"]:
        
        nombre = request.GET["nombre"]
        
        ciudad = Equipo.objects.filter(nombre_icontains=nombre)
             
        #respuesta= f"Estoy buscando al equipo {request.GET['nombre']}"
        
        return render(request, "AppCoder/resultadoBusqueda.html", {"nombre":nombre,"ciudad":ciudad})
        
    else:
        
        respuesta= "Che mandame info para buscar"
    
    return HttpResponse(respuesta)


def busquedaEquipo(request):
    
    return render(request, 'AppCoder/busquedaEquipo.html')

def estadioFormulario(request):
    
    #de aca se obtiene una direccion y el anio de fundacion
    
    #si alguien ya completo ese formulario entra al if, pero si nadie completo aun el form, entra al else
    # y crea el formulario / ese form es el que hacemos que viaje al html, es por eso que en el html yo puedo
    # recoger a ese form, porq ya lo instancie a ese form en else
    
    if request.method == "POST":
        
        miFormulario = EstadioFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
        
            estadioInsta = Estadio(direccion=informacion["direccion"], anioFund=informacion["anioFund"])
            
            estadioInsta.save() #este save es el que guarda en la BD, como hacia en la terminal
            
            return render(request, 'AppCoder/inicio.html') #o sea una vez que lo guarde me lleva al inicio nuevamente
        
    #si no me envian el post voy a hacer esto: crear el formulario vacio, instancia de la clase que yo genere
        
    else:
        
        miFormulario = EstadioFormulario()
        

    # return HttpResponse("Esto es una prueba de inicio")   
    return render(request, 'AppCoder/estadioFormulario.html',{"miFormulario":miFormulario})

#primer vista:
def inicio(request):
    # return HttpResponse("Esto es una prueba de inicio")
    
    return render(request, 'AppCoder/inicio.html')

#segunda vista:
def jugadores(request):
    # return HttpResponse("Esto es una prueba de inicio")
    
    return render(request, 'AppCoder/jugadores.html')

#tercers vista:
def curso(request):
    # return HttpResponse("Esto es una prueba de inicio")
    
    return render(request, 'AppCoder/curso.html')

def equipos(request):
    # return HttpResponse("Esto es una prueba de inicio")
    
    return render(request, 'AppCoder/equipos.html')

def estadio(request):
    # return HttpResponse("Esto es una prueba de inicio")
    
    return render(request, 'AppCoder/estadio.html')