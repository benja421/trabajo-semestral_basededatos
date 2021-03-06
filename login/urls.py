from django.contrib import admin
from django.urls import path, include
from .views import admin_reg, eliminar_mascota, eliminar_usuario, inicio,inicio_sesion, mascota_modificacion, mascota_registro, menu_usuario, modificar_usuario,registra_admin,menu_admin,menu_medico,registro_mascota,recuperar_pass,cambiar_pass,cambiar_datos,lista_usuario,perfil_medico,mascota_historial,mascota_modificar,modificacion_usuario


urlpatterns = [
    path('',inicio,name="inicio"),
    path('inicio_sesion', inicio_sesion, name="inicio_sesion"),
    path('registra_admin/',registra_admin,name="registra_admin"),
    path('admin_reg/',admin_reg,name="admin_reg"),
    path('menu_admin/',menu_admin,name="menu_admin"),
    path('menu_medico/',menu_medico,name="menu_medico"),
    path('menu_usuario/',menu_usuario,name="menu_usuario"),
    path('registro_mascota/',registro_mascota,name="registro_mascota"),
    path('recuperar_pass/',recuperar_pass,name="recuperar_pass"),
    path('cambiar_pass/',cambiar_pass,name="cambiar_pass"),
    path('cambiar_datos/',cambiar_datos,name="cambiar_datos"),
    path('lista_usuario/',lista_usuario,name="lista_medicos"),
    path('perfil_medico/',perfil_medico,name="perfil_medico"),
    path('mascota_historial/',mascota_historial,name="mascota_historial"),
    path('mascota_modificar/<int:id>',mascota_modificar,name="mascota_modificar"),
    path('mascota_modificacion/',mascota_modificacion, name="mascota_modificacion"),
    path('eliminar/<int:id>',eliminar_usuario, name="eliminar_usuario"),
    path('Eliminar/<int:id>',eliminar_mascota, name="eliminar_mascota"),
    path('mascota_registro/',mascota_registro, name="mascota_registro"),
    path('modificar_usuario/<int:id>', modificar_usuario, name="modificar_usuario"),
    path('modificacion_usuario', modificacion_usuario, name="modificacion_usuario"),
]

