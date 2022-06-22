from django.urls import path
from rest_veterinaria.views import addAtenciones, addComuna, lista_atenciones, lista_comuna, lista_mascotas, addMascota, modEliminarAtenciones, modEliminarComuna, modEliminarMascota
from rest_veterinaria.viewsLogin import ini_user

urlpatterns = [
    path('lista_mascotas/',lista_mascotas,name="lista_mascotas"),
    path('addMascota/',addMascota,name="addMascota"),
    path('modEliminarMascota/<codigo>',modEliminarMascota,name="modEliminarMascota"), 
    path('ini_user/',ini_user,name="ini_user"),
    path('lista_comuna/',lista_comuna,name="lista_comuna"),
    path('addComuna/',addComuna,name="addComuna"),
    path('modEliminarComuna/<codigo>',modEliminarComuna,name="modEliminarComuna"), 
    path('lista_atenciones/',lista_atenciones,name="lista_atenciones"),
    path('addAtenciones/',addAtenciones,name="addAtenciones"),
    path('modEliminarAtenciones/<codigo>',modEliminarAtenciones,name="modEliminarAtenciones"), 
]
#lista(get) listo aa453698c726866340fc485b579891b5f4bbea05
#agregar(post) listo
#modificar(put) listo
#eliminar listo
#seguridad listo