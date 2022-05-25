from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'login/Principal_usuario.html')
        

def inicio_sesion(request):
    return render(request,'login/inicio_sesion.html')

def registra_admin(request):
    return render(request,'login/registrar_admin.html')

def registra_medico(request):
    return render(request,'login/registro_medico.html')

def menu_admin(request):
    return render(request,'login/menu_admin.html')

def menu_medico(request):
    return render(request,'login/menu_medico.html')

def registro_mascota(request):
    return render(request,'login/mascota_registrar.html')

def recuperar_pass(request):
    return render(request,'login/pass_recup.html')

def cambiar_pass(request):
    return render(request,'login/cam_pass.html')

def cambiar_datos(request):
    return render(request,'login/cambiar_datos.html')

def lista_medicos(request):
    return render(request,'login/medicos.html')

def perfil_admin(request):
    return render(request,'login/perfil_admin.html')

def perfil_medico(request):
    return render(request,'login/perfil_medico.html')

def mascota_historial(request):
    return render(request,'login/mascota_historal.html')

def mascota_modificar(request):
    return render(request,'login/mascota_modif.html')

