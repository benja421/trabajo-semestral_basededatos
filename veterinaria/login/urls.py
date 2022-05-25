from django.contrib import admin
from django.urls import path
from .views import inicio,inicio_sesion,registra_admin,registra_medico,menu_admin,menu_medico,registro_mascota,recuperar_pass,cambiar_pass,cambiar_datos,lista_medicos,perfil_admin,perfil_medico,mascota_historial,mascota_modificar

urlpatterns = [
    path('',inicio,name="inicio"),
    path('inicio_sesion/',inicio_sesion,name="inicio_sesion"),
    path('registra_admin/',registra_admin,name="registra_admin"),
    path('registra_medico/',registra_medico,name="registra_medico"),
    path('menu_admin/',menu_admin,name="menu_admin"),
    path('menu_medico/',menu_medico,name="menu_medico"),
    path('registro_mascota/',registro_mascota,name="registro_mascota"),
    path('recuperar_pass/',recuperar_pass,name="recuperar_pass"),
    path('cambiar_pass/',cambiar_pass,name="cambiar_pass"),
    path('cambiar_datos/',cambiar_datos,name="cambiar_datos"),
    path('lista_medicos/',lista_medicos,name="lista_medicos"),
    path('perfil_admin/',perfil_admin,name="perfil_admin"),
    path('perfil_medico/',perfil_medico,name="perfil_medico"),
    path('mascota_historial/',mascota_historial,name="mascota_historial"),
    path('mascota_modificar/',mascota_modificar,name="mascota_modificar"),
    
]