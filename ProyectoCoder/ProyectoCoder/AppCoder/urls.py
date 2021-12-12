from django.urls import path
from AppCoder import views

urlpatterns = [
        
    path('inicio/', views.inicio, name="Inicio"),
    path('jugadores/', views.jugadores, name='Jugadores'),
    path('curso/', views.curso),
    path('equipos/', views.equipos, name='Equipos'),
    path('estadio/', views.estadio, name='Estadio'),
    path('estadioFormulario/', views.estadioFormulario, name='EstadioFormulario'),
    path('busquedaEquipo/', views.busquedaEquipo, name='BusquedaEquipo'),
    path('buscar/', views.buscar, name='Buscar'),
    
]