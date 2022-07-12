from http.client import responses
from urllib import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from login.models import Mascota, Comuna, Atenciones
from .serializers import MascotaSerializers, ComunaSerializers, AtencionesSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Mascota
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_mascotas(request):
    if request.method == 'GET':
        mascota = Mascota.objects.all()
        serializador = MascotaSerializers(mascota, many=True)
        return Response(serializador.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializador = MascotaSerializers(data = data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializador.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addMascota(request):
    data = JSONParser().parse(request)
    serializer = MascotaSerializers(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modEliminarMascota(request,codigo):
    try:
        m = Mascota.objects.get(codigoChip = codigo)
    except Mascota.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MascotaSerializers(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = MascotaSerializers(m, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
#Comuna
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_comuna(request):
    if request.method == 'GET':
        comuna = Comuna.objects.all()
        serializador = ComunaSerializers(comuna, many=True)
        return Response(serializador.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializador = ComunaSerializers(data = data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializador.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addComuna(request):
    data = JSONParser().parse(request)
    serializer = ComunaSerializers(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modEliminarComuna(request,codigo):
    try:
        c = Comuna.objects.get(idComuna = codigo)
    except Comuna.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ComunaSerializers(c)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = ComunaSerializers(c, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        c.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#Atenciones

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_atenciones(request):
    if request.method == 'GET':
        atencion = Atenciones.objects.all()
        serializador = AtencionesSerializers(atencion, many=True)
        return Response(serializador.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializador = AtencionesSerializers(data = data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializador.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addAtenciones(request):
    data = JSONParser().parse(request)
    serializer = AtencionesSerializers(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modEliminarAtenciones(request,codigo):
    try:
        a = Atenciones.objects.get(idComuna = codigo)
    except Atenciones.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AtencionesSerializers(a)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = AtencionesSerializers(a, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        a.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)