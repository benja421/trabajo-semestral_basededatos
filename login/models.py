
from django.db import models

# Create your models here.

class Rol(models.Model):
    codigo = models.IntegerField(primary_key=True, verbose_name='Codigo de usuario')
    tipoUsuario = models.CharField(max_length=20,verbose_name='Tipo de usuario', blank=False, null=False)
    
    def __str__(self):
        return self.tipoUsuario


class Usuario(models.Model):
    idusu = models.AutoField(primary_key=True, verbose_name='Codigo de usuario')
    nombreUsuario = models.CharField(max_length=20,verbose_name='Nombre del usuario')
    apellidoUsuario = models.CharField(max_length=20,default='apellido',verbose_name='Apellido del usuario')
    contra = models.CharField(max_length=30,verbose_name='Contraseña del usuario')
    correo = models.EmailField(verbose_name='Correo del usuario')
    fechNacimiento = models.DateTimeField(verbose_name='Fecha de nacimiento', null=True)
    foto = models.ImageField(upload_to="usuario", null=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def _str_(self):
        return self.nombreUsuario


class Atenciones (models.Model):
  numtratamiento = models.IntegerField(primary_key=True,default=1, verbose_name='numero tratamiento')
  nombreTratamiento = models.CharField(max_length= 35,verbose_name='Tratamiento')
  
  

  def __str__(self):
     return self.nombreTratamiento

class Comuna (models.Model):
  idComuna = models.IntegerField(primary_key=True ,default=1,verbose_name= 'id de la comuna')
  nombreComuna = models.CharField(max_length=40, verbose_name='nombre de la comuna')

  def _str_(self):
      return self.nombreComuna

class Mascota (models.Model):
  codigoChip = models.IntegerField(primary_key=True, verbose_name= 'Chip de la Mascota')
  nombreMascota = models.CharField(max_length=20,verbose_name='Nombre de la mascota')
  edad = models.IntegerField(verbose_name='Edad de la mascota')
  nombreDuennio = models.CharField(max_length=20,default='nombre',verbose_name='nombre del dueño')
  comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
  atencion = models.ForeignKey(Atenciones, on_delete=models.CASCADE)
  

  def _str_(self):
      return self.nombreMascota