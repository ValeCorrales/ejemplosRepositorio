from django.forms.models import fields_for_model
from django.shortcuts import render

from django.http import HttpResponse
from AppCoder import forms
from AppCoder.forms import EstadioFormulario, EmpleadoFormulario, JugadorFormulario, UserRegisterForm, AvatarFormulario

from AppCoder.models import Avatar, Equipo, Estadio, Jugador, Empleado, Curso




# Create your views here.


#avatar: es una imgaen, un logo, algo que acompania al logeo - para eso hay que crear un modelo
#que se va a llamar avatar y va a tener una relacion..
#las imagenes, los sonidos, los videos, todo lo que trae archivo externo: hay queguardarlo
#en una carpeta, por defecto se suele guardar en una carpeta qeu se llama media - la cual hay que crearla
#al mismo nivel que la app y el proyecto
#tambien hay que configurar las configuraciones de Django para que pueda accedder a esas imagenes, esto 
#se hace en settings.py: se agrega media url y media root(para eso hay que importar os) - despues agregamos
# a nuestras url patterns del PROYECTO STATIC(Media url y media root) - PARA ESTO HAY que importar
# static y settinggs
#como modificamos el modelo, hay que importarlo con magemigrations y migrate
#para que aparezca en admin, hay que migrarlo en addmin.py 
#hasta aca puedo hacer crud desde el panel de adminitracion, pero si quiero que cualquiera pueda
#agregar un avatar, hay que hacer leer, modificar, etc..
#para que me mmuestre el avatar, agrego en el html - para eso en la vista que quiero que se vea mi imagen
#en este caso en inicio cuanod me dicce bienvenido,  agrego el avatar por medio de un diccionario
#en la vista de inicio agrego un codigo, en el html que lo quiero mostrar tambein
#por ultimo agrego una vista (que tenes que estar logeado) para que los usuarios puedan agregar avatar:

from django.contrib.auth.models import User

def agregarAvatar(request):
    
    #si alguien ya completo ese formulario entra al if, pero si nadie completo aun el form, entra al else
    # y crea el formulario / ese form es el que hacemos que viaje al html, es por eso que en el html yo puedo
    # recoger a ese form, porq ya lo instancie a ese form en else
    
    if request.method == "POST":
        
        miFormulario = AvatarFormulario(request.POST, request.FILES) #aca me llega toda la info del html
        
        if miFormulario.is_valid(): #si pasa la vlaidacion de Django
            
            u= User.objects.get(username=request.user)
            
            avatar = Avatar (user = u, imagen= miFormulario.cleaned_data['imagen'])
            
            avatar.save() #este save es el que guarda en la BD, como hacia en la terminal
            
            return render(request, 'AppCoder/inicio.html') #o sea una vez que lo guarde me lleva al inicio nuevamente
        
    #si no me envian el post voy a hacer esto: crear el formulario vacio, instancia de la clase que yo genere
        
    else: #entra al else si es la primera vez que entras a la web
        
        miFormulario = AvatarFormulario()
        

    # return HttpResponse("Esto es una prueba de inicio")   
    return render(request, 'AppCoder/avatarFormulario.html',{"miFormulario":miFormulario})


#login:uno no quiere que todo el mundo tenga acceso a todo, hasta ahora cualquiera que tenga la url
#podia entrar, modificar, borrar, hacer todo - con un login: unas personas pueden hacer unas cosas
#y otros usarios otras - superusuario o creador de la pagina puede crear objetoss ponele: dar altas o eliminar
#pero otros pueden solo ver o buscar, para eso necesitamos el login: hay 2 formas de hacerlo:
#si sos el superadmin en el panel de usuario pones: users pones add y lo agregas, le creas un usuario 
# con contrasenia y le pones que es lo que quiero que haga / TENES QUE SER SUPERUSUARIO SINO NO PODES
# ENTRAR AL PANEL DE ADMINISTRACION

#SEGUNDA MANERA DESDE LA WEB, SIN SER SUPER USUARIO: generar vista, url y html
#1 crear template html con metodo post, en action no le ponemos nada, ponemos el token de siempre,
# despues ponermos form as table o parrafo, y el input con type submit y seguido del nombre del "boton"
#2 crear la url: login
#3 crear vista: loguin_request: antes importar autenticationform y login, logout, authenticate..:

# tambien hay que hacer crud con el login, o sea dar de alta usuarios, para eso ahcemos un form
#para esto hay que ahcer:vista (registro con metodo post sino hace otra cosa en el else)
#para hace la vista de register hay que importar en forms.py usercreation form 
# y crear una clase que se llame UserRegisterForm(UserCreationform), despues esto en view lo importas
# cmo los otros formulario que creamos



def register(request):
    if request.method == "POST":
        
        #form = UserCreationForm(request.POST) - no se porq ponemos esto!!
        form = UserRegisterForm(request.POST)  # se genera el form con los datos que vinieron del form,
        #esto es un formulario que hay que importarlo
        
        #si el form es valido:
        
        if form.is_valid():
            username=form.cleaned_data["username"] #del formulario agarro al username - esto es para ponerlo
            #por ejemplo en el return render, en el mensaje agarro el username, sino ni lo pongo
            form.save() #el form es una instancia del UserRegisterForm (que esto es el formulario de usuario),
            #si yo salvo el form lo que estoy haciendo es guardar en mi base de datos el usuairo que se
            #acaba de crear, o sea de regestar - modelo user
            
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenidooo {username} - tu usuario fue creado!!!"})
    
    else: #si la request no tenia un metodo post, se genera el userregisterform
        
        #form = UserCreationForm() - no se porq ponemos esto!!
        form= UserRegisterForm()
        
    return render(request, "AppCoder/register.html", {"form": form})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
    
    if request.method=="POST": #si recibi un post de la request hago este y sino mme voy al else
    
        form = AuthenticationForm(request, data = request.POST)
        
        #el formulario de autenticacion: o sea AutgenticationForm tiene determinados parametros que hay 
        #que respetar, por ejemplo: username y password que vamos a usar abajo
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            #la variable"usuario" es una variable interna, la llamamos como queremos, lo que SI 
            #hay que mantener el nombre es de "username" - lo que estoy haciendo aca es traer
            #la data del username
            contrasenia= form.cleaned_data.get("password")
            
            #despues genero una variables user, pero del tipo autenticacion, o sea estoy generando
            #una variable de autenticacion qeu recibe un usario y una contrasenia:
            
            user = authenticate(username=usuario, password=contrasenia)
            
            #si el usuario no esta vacio, hacemos la "bienvenida del usuario"
            if user is not None: # o sea si NO es vacio, es decir tiene datos: generamos el elemento login
                                    #y hago el request user:
                login(request, user)
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenidooo {usuario}!!!"})
            
            #sino le digo datos incorrectos, volve a cargar:

            else:
            
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos, Volve a logearte!!"})
          
        # si el formulario no es valido, o sea no paso la prueba de validacion cuando pusimos 
        # is valid():  
        else:
                   return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo!!"})
    
    form = AuthenticationForm #se genera el formulario vacio, o sea sin nada para hacer el login
    
    return render (request, "AppCoder/login.html", {"form":form})


#CBV: clases basadas en vistas: hacers crud con cursos (lo mismo que hicimos con jugador pero con la 
# herramienta que te da django) - como se llama clases basadas en vistas, en vez de crear vistas
#vamos a crear clases

#importamos todo esto:

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

#lista de curso - equivale a LEER - esta clase nos da todos los cursos - object filter all que traia todos
#los elementos de la base de datos
class CursoList(ListView): #este te lleva al curso list, en template name lo dice
    
    model = Curso # a djnago le decis: modelo con el que vas a trabajar
    template_name = "AppCoder/cursos_list.html" #a djando le decis: template con el que vas a trabajar
    #esto de template name: es donde esta el template que queres que te renderise con el cursoList, osea
    # es el return render
    

#Detalle - super leer, es como un buscar tambien
class CursoDetalle(DetailView): #este te lleva al curso detalle, en template name lo dice
    
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

#crear elementos
class CursoCreacion(CreateView): #este te lleva al curso_form, se ve qe el CreateViwe tiene asociado
    #el template curso_form, porque si ves no ponemos template name en este caso a diferencia de los
    #dos anteriores
    
    model = Curso
    success_url = "AppCoder/curso/list" # cuando terminas de crear el curso volve a: la lista de cursos
    #o sea le pones a donde queres que te redireccione, es una URL, no un template!
    #LOS DOS PUNTITOS QUIEREN DECIR: volver dos direcciones atras - sino podes poner: import reverse_lazy
    #y ahi pones en vez de los pntitos: AppCoder, o sea las opciones de url son:
    # "AppCoder/curso/list" p "../curso/list"
    fields = ["nombre", "camada", "esNoche"] #estos son los elementos que quiero que se carguen, o sea
    #los atributos de elementos lo hace django tambien
    
#modificar: update

class CursoUpdate(UpdateView): #este te lleva al curso_form tambien
    
    
    model = Curso
    success_url = "AppCoder/curso/list" # cuando terminas de modificar el curso vuelve a: la lista de cursos
    fields = ["nombre", "camada", "esNoche"] #le decis cuales son los atributos que puede modificar, en este
    #caso pusimos todos, si queres algunos pones solo esos
    
#Borrar
class CursoDelete(DeleteView): #este te lleva al curso_confirm_delete, se ve qe el DeleteView tiene asociado
    #ese template porq si ves no ponemos template name en este caso 
    
    
    model = Curso
    success_url = "AppCoder/curso/list" # cuando terminas de modificar el curso vuelve a: la lista de cursos

def empleadoFormulario(request):
       
    #si alguien ya completo ese formulario entra al if, pero si nadie completo aun el form, entra al else
    # y crea el formulario / ese form es el que hacemos que viaje al html, es por eso que en el html yo puedo
    # recoger a ese form, porq ya lo instancie a ese form en else
    
    if request.method == "POST":
        
        miFormulario = EmpleadoFormulario(request.POST)
        
        if miFormulario.is_valid(): 
            
            informacion = miFormulario.cleaned_data
        
            emple = Empleado(    
                             
                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                dni =  informacion["dni"],
                profesional = informacion["profesional"],
                fechaDeNacimiento = informacion["fechaDeNacimiento"],
             #mandar la informacion por parametros por no por posicion!!          
             #por posicion seria respetando el orden osea seria: informacion["nombre"], informacion["apellido"],  etc 
            )
            
            emple.save() #este save es el que guarda en la BD, como hacia en la terminal
            
            return render(request, 'AppCoder/inicio.html') #o sea una vez que lo guarde me lleva al inicio nuevamente
        
    #si no me envian el post voy a hacer esto: crear el formulario vacio, instancia de la clase que yo genere
        
    else: #entra al else si es la primera vez que entras a la web
        
        miFormulario = EmpleadoFormulario()
        

    # return HttpResponse("Esto es una prueba de inicio")   
    return render(request, 'AppCoder/empleadoFormulario.html',{"miFormulario":miFormulario})
    
def eliminarJugador(request, jugador_apellido):
    
    jugadorQueQuieroBorrar = Jugador.objects.get(apellido=jugador_apellido) #solo traigo el que tiene el apellido
    #pide por parametro
    
    jugadorQueQuieroBorrar.delete()    
    
    jugadores = Jugador.objects.all()    #traigo a todos los jugadores, sin el que borramos si hicimos bien
    
    return render(request, "AppCoder/leerJugadores.html", {"jugadores":jugadores})



def editarJugador(request, numero_para_editar): #aca lo qeu estos haciendo es enviar por aprametros
    #el ajugador qeu quiero modificar
    #numero_para_editar: no es el numero de la camiseta! es el numero identificador del jugador
    #que se va a editar - es lo que se llama el id del modelo de la tabla - dni: clave primaria del objeto
    #el id es unico, no se repite, o sea no es que sean numeros consecutivos que si borras uno el
    #id del otro cambia  - ES EL DOC DEL OBJETO, UN CODIGO UNICO
    
    #tenemos que traer de la BD el jugador que quiero borrar - creo un jug igual que en eliminar
    
    jugador = Jugador.objects.get(numero=numero_para_editar)
    
    #editar jugador tiene dos posibilidades: venir con el post o sin el post
    #si viene sin el post, o sea si no hice el post, llena el formulario con los datos de ese jugador
    #si hice el post, ademas de enviar el form con esos datos, lo hago en miFormulario = ..
    #salvo el form con los datos de jugador. bla bla
    
    #teniamos el boton eliminar, ahora vamos a agregar el de editar
    
    if request.method == "POST":
        
        miFormulario = JugadorFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
        
            jugador.apellido=informacion["apellido"] 
            jugador.numero=informacion["numero"]
            jugador.esBueno=informacion["esBueno"]
            
            jugador.save() #este save es el que guarda en la BD, como hacia en la terminal
            #como el id es el q trae de la BD, y yo nunca lo cambie, no me guarda un nuevo jugador
            #sino que se salvan estos datos modificados
            
            juga = Jugador.objects.all()    
            
            return render(request, 'AppCoder/leerJugadores.html') 
        
    #antes si no me envian el post voy a crear el formulario vacio, instancia de la clase que yo genere
    #pero ahora loq ue voy a generar es un form con campos
        
    else:
        #mandamos valores iniciales con initial en un dicc, todos los atrib
        #o sea llenamos el form con los datos que tenemos guardados
        miFormulario = JugadorFormulario(initial={"apellido":jugador.apellido, "numero": jugador.numero, "esBueno": jugador.esBueno})
        

    # return HttpResponse("Esto es una prueba de inicio")  
    #en el render enviamos el formulario y el parametro que quiero editar mediante el dicc 
    return render(request, 'AppCoder/editarJugador.html',{"miFormulario":miFormulario, "numero_para_editar": numero_para_editar})



def jugadorFormulario(request):
    
    #de aca se obtiene una direccion y el anio de fundacion
    
    #si alguien ya completo ese formulario entra al if, pero si nadie completo aun el form, entra al else
    # y crea el formulario / ese form es el que hacemos que viaje al html, es por eso que en el html yo puedo
    # recoger a ese form, porq ya lo instancie a ese form en else
    
    if request.method == "POST":
        
        miFormulario = JugadorFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
        
            jugadores = Jugador(apellido=informacion["apellido"], numero=informacion["numero"], esBueno=informacion["esBueno"])
            
            jugadores.save() #este save es el que guarda en la BD, como hacia en la terminal
            
            jugadores = Jugador.objects.all()    
            
            return render(request, 'AppCoder/leerJugadores.html') 
        
    #si no me envian el post voy a hacer esto: crear el formulario vacio, instancia de la clase que yo genere
        
    else:
        
        miFormulario = JugadorFormulario()
        

    # return HttpResponse("Esto es una prueba de inicio")   
    return render(request, 'AppCoder/jugadorFormulario.html',{"miFormulario":miFormulario})


def leerJugadores(request):
    
    jugadores = Jugador.objects.all() #esto trae todo los jugadores de la base de datos
    
    #si quiero que esto se vea tengo que generar un contexto, para eso creo un diccionario
    
    dir = {"jugadores":jugadores} #contexto
    
    return render(request, "AppCoder/leerJugadores.html", dir)
    

def busquedaEquipo(request):
    
    return render(request, "AppCoder/busquedaEquipo.html")

def buscar(request):
    
    if request.GET["nombre"]:
        
        nombre = request.GET["nombre"]
        
        equipos   = Equipo.objects.filter(nombre__icontains=nombre)
             
        #respuesta= f"Estoy buscando al equipo {request.GET['nombre']}"
        
        return render(request, 'AppCoder/resultadoBusqueda.html', {"equipos":equipos,"nombre":nombre})
        
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
    
    diccionario = {}
    cantidadDeAvatares = 0
    
    if request.user.is_authenticated: #si el usuario esta autenticado - podes hacer esto o un decorador
                                      #un decorador es ponerle un @login o algo asi
    #de la request agarro al usuario qeu esta registrado, agarro el id, y ccon el filter traigo todos los 
    #avatares, de la persona que esta registrada: en resumen:  trae todos los objetos (avatares) filtrados 
    # por el usuario que esta registrado
        print("Entre al if")
        avatar=Avatar.objects.filter(user=request.user.id)
        
        for a in avatar: #me fijo cuantos avatares tiene 
            cantidadDeAvatares= cantidadDeAvatares +1 
            
        diccionario["avatar"]= avatar[cantidadDeAvatares-1].imagen.url #cantidad - 1 es para que me muestre
        #el ultimo avatar - la clave diccionario se llama avatar
    
    
    return render(request, 'AppCoder/inicio.html', diccionario) 
    
    #antes en vesz de diccionario habiamos puesto: {"url":avatar[0].imagen.url}) - el 0 es porque si cargaron
#varias fotos, quiere decir quedarse con el rpimer elemento de mis avateres, para que no te muestre todos
#el .url es porque yo lo que quiero es la url, no la imgen en si

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