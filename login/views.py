from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Rol,Usuario,Mascota,Atenciones,Comuna

# Create your views here.
def inicio(request):
    return render(request,'login/Principal_usuario.html')
        

def inicio_sesion(request):
    return render(request,'login/inicio_Sesion.html')

def admin_reg(request):
    rol = Rol.objects.all()
    contexto = {"rol":rol}
    return render(request, 'login/registrar_admin.html', contexto)
    
def registra_admin(request):
    nombreUsuario_us = request.POST['nombre']
    apellido_us = request.POST['apellido']
    contra_us = request.POST['pass']
    correo_us = request.POST['email']
    fechNacimiento_us = request.POST['fechaN']
    foto_us = request.FILES['foto_u']
    rol_m = request.POST['cod']
    rol_c = Rol.objects.get(codigo = rol_m)    
    
    #insert
    Usuario.objects.create( 
                            nombreUsuario = nombreUsuario_us,
                            apellidoUsuario = apellido_us, 
                            contra= contra_us, 
                            correo = correo_us,
                            fechNacimiento =fechNacimiento_us, 
                            foto= foto_us, 
                            rol = rol_c)

    messages.success(request,'Admin registrado')

    return redirect('menu_admin')

def menu_admin(request):
    return render(request,'login/menu_admin.html')

def menu_medico(request):
    return render(request,'login/menu_medico.html')

def menu_usuario(request):
    return render(request,'login/menu_usuario.html')

#envio de contexto a registro
def registro_mascota(request):
    
    comuna = Comuna.objects.all()
    atenciones = Atenciones.objects.all()
    contexto = {
        "comuna": comuna, 
        "atenciones" : atenciones}
    

    return render(request,'login/mascota_registrar.html',contexto)

def mascota_registro(request):
    numerochip = request.POST['nchip']
    nombre_mascot   = request.POST['nombremas']
    nombre_due  = request.POST['nombredue']
    edad_masc   = request.POST['edadmasc']
    comuna  = request.POST['comuna']
    tratamiento = request.POST['atratamiento']
    comuna_a = Comuna.objects.get(idComuna = comuna)
    atenciones = Atenciones.objects.get(numtratamiento = tratamiento)

    Mascota.objects.create( codigoChip = numerochip,
                            nombreMascota = nombre_mascot,
                            edad = edad_masc,
                            nombreDuennio= nombre_due,
                            comuna = comuna_a,
                            atencion = atenciones

    )
    


    messages.success(request,'Mascota registrado')
    return redirect('menu_medico')

def recuperar_pass(request):
    return render(request,'login/pass_recup.html')

def cambiar_pass(request):
    return render(request,'login/cam_pass.html')

def cambiar_datos(request):
    return render(request,'login/cambiar_datos.html')

def lista_usuario(request):
    usuario = Usuario.objects.all()
    contexto = {"usuario":usuario}
    return render(request,'login/medicos.html', contexto)

#eliminar mascota
def eliminar_mascota(request, id):
    mascota1 = Mascota.objects.get(codigoChip = id)
    mascota1.delete()
    messages.success(request,'Mascota Eliminada')

    return redirect('/mascota_historial/')

#eliminar usuario o mascota
def eliminar_usuario(request, id):
    try:
        usuario1 = Usuario.objects.get(idusu = id)
        usuario1.delete()
        messages.success(request,'Usuario Eliminada')

        return redirect('/lista_usuario/')
    except:
        mascota1 = Mascota.objects.get(codigoChip = id)
        mascota1.delete()
        messages.success(request,'Mascota Eliminada')

        return redirect('/mascota_historial/')
    
#modificar usuario 1
def modificar_usuario(request, id):
    usuario1 = Usuario.objects.get(idusu = id) # obtengo los datos de la mascota
    rol1 = Rol.objects.all() #obtener todas las razas para llenar el combobox

    contexto = {
        "usuario" : usuario1,
        "rol" : rol1
    }

    return render(request,'login/modificar_usuario.html',contexto)

#modificar usuario 2
def modificacion_usuario(request):
    id = request.POST['id']
    nombreUsuario_us = request.POST['nombre']
    apellido_us = request.POST['apellido']
    contra_us = request.POST['pass']
    correo_us = request.POST['email']
    fechNacimiento_us = request.POST['fechaN']
    foto_us = request.FILES['foto_u']
    rol_m = request.POST['cod']
    
    usuario = Usuario.objects.get(idusu = id)
    usuario.nombreUsuario = nombreUsuario_us
    usuario.apellidoUsuario = apellido_us
    usuario.contra = contra_us
    usuario.correo = correo_us
    usuario.fechNacimiento = fechNacimiento_us
    usuario.foto = foto_us
    
    rol = Rol.objects.get(codigo = rol_m)
    usuario.rol = rol
    
    usuario.save() #el upadate

    messages.success(request, 'usuario Modificada')
    return redirect('menu_admin')

def perfil_admin(request):
    return render(request,'login/perfil_admin.html')

def perfil_medico(request):
    return render(request,'login/perfil_medico.html')


def mascota_historial(request):    
    mascotas = Mascota.objects.all()
    comuna = Comuna.objects.all()
    atencion = Atenciones.objects.all() 
    contexto = {"mascota":mascotas, "comuna": comuna, "atencion":atencion}
    
    return render(request,'login/mascota_historal.html',contexto)

#ir a la pagina de modificar
def mascota_modificar(request,id):
    mascota = Mascota.objects.get(codigoChip = id)
    comuna = Comuna.objects.all()
    atencion = Atenciones.objects.all()

    contexto = {
        "mascota" : mascota,
        "comuna" : comuna,
        "atencion" : atencion
    }

    return render(request,'login/mascota_modif.html', contexto)

def mascota_modificacion(request):
    numerochip = request.POST['nchip']
    nombre_mascot   = request.POST['nombremas']
    nombre_due  = request.POST['nombredue']
    edad_masc   = request.POST['edadmasc']
    comuna  = request.POST['comuna']
    tratamiento = request.POST['atratamiento']


    mascota = Mascota.objects.get(codigoChip = numerochip)
    mascota.codigoChip = numerochip
    mascota.nombreMascota = nombre_mascot
    mascota.nombreDuennio = nombre_due
    mascota.edad = edad_masc
    
    
    comuna2 = Comuna.objects.get(idComuna = comuna)
    mascota.comuna = comuna2
    
    atencion = Atenciones.objects.get(numtratamiento = tratamiento)
    mascota.atencion = atencion
    
    mascota.save() #el upadate

    messages.success(request, 'usuario Modificada')
    
    return redirect('menu_medico')

