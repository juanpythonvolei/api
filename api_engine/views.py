from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serealizers import *
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@api_view(['GET'])
def consultar_clientes(request):
  if request.method == 'GET':
    usuarios = Usuarios.objects.all()
    serializer = UsuariosSerializer(usuarios,many=True)
    return Response(serializer.data)
  else:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
@api_view(['GET'])
def consultar_clientes_por_site(request,site):
  if request.method == 'GET':
    try:
      usuarios = Usuarios.objects.get(nome_site = site)
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UsuariosSerializer(usuarios)
    return Response(serializer.data)
  else:
    return Response(status=status.HTTP_404_NOT_FOUND)  
  
@api_view(["PUT","DELETE"])
def manipular_usuario(request,user):
  if request.method == 'PUT':
    if user:
      usuario_a_modificar = Usuarios.objects.get(nome_site=user)
    else:
      usuario_a_modificar = Usuarios.objects.get(nome_site=request.data['nome_site'])
    serializer = UsuariosSerializer(usuario_a_modificar,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    else:
      return Response(status=status.HTTP_400_BAD_REQUEST)
    
  if request.method =='DELETE':
    usuario_a_se_deletar = Usuarios.objects.get(nome_site=user)
    usuario_a_se_deletar.delete()
    return Response(status.HTTP_202_ACCEPTED)
  
@api_view(['POST'])
def criar_usuario(request):
    novo_usuario = request.data
    print(novo_usuario)
    serializer = UsuariosSerializer(data=novo_usuario)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
      return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def acessar(request):
  if request.method == 'POST':
    nome = request.data['nome_site']
    senha = request.data['senha']
    try:
      Usuarios.objects.get(nome=nome,senha=senha)
      return Response(status=status.HTTP_200_OK)
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)

