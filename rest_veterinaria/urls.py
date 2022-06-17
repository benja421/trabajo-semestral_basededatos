from django.urls import path
from rest_veterinaria.views import lista_mascotas, addMascota, modEliminarMascota
from rest_veterinaria.viewsLogin import ini_user

urlpatterns = [
    path('lista_mascotas/',lista_mascotas,name="lista_mascotas"),
    path('addMascota/',addMascota,name="addMascota"),
    path('modEliminarMascota/<codigo>',modEliminarMascota,name="modEliminarMascota"), 
    path('ini_user/',ini_user,name="ini_user"),
]
#lista listo
#agregar falta test
#modificar(put) falta test
#eliminar listo
#seguridad no implementado