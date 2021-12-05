from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

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