from django.urls import path
from AppCoder import views

urlpatterns = [
        
    path('inicio/', views.inicio, name="Inicio"),
    path('jugadores/', views.jugadores, name='Jugadores'),
    path('curso/', views.curso),
    path('equipos/', views.equipos, name='Equipos'),
    path('estadio/', views.estadio, name='Estadio'),
    path('estadioFormulario/', views.estadioFormulario, name='EstadioFormulario'),
    path('busquedaEquipo/', views.busquedaEquipo),
    path('buscar/', views.buscar),
    path('empleadoFormulario/', views.empleadoFormulario),
    path('leerJugadores/', views.leerJugadores, name='LeerJugadores'),
    path('jugadorFormulario/', views.jugadorFormulario, name='JugadorFormulario'),
    path('eliminarJugador/<jugador_apellido>/', views.eliminarJugador, name='EliminarJugador'),
    path('editarJugador/<numero_para_editar>/', views.editarJugador, name='EditarJugador'),
    
    #PARA CLASES BASADAS EN LISTAS: 
    path('curso/list/', views.CursoList.as_view(), name='List'), #es el de leer
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'), #se ve fea: pk es primary key del elemento
    
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'), #esta url es para crear
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    
    #clase 23:
    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('agregarAvatar/', views.agregarAvatar, name='AgregarAvatar'),
    
    
]