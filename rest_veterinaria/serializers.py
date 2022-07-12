from dataclasses import fields
from rest_framework import serializers
from login.models import Atenciones, Mascota, Comuna

class MascotaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['codigoChip','nombreMascota','edad','nombreDuennio','comuna','atencion']

class ComunaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields= ['idComuna','nombreComuna']

class AtencionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Atenciones
        fields = ['numtratamiento', 'nombreTratamiento']