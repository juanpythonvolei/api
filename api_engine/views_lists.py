from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serealizers import ListasSerializer,ParticipacoesSerializer
import json



@api_view(['POST','DELETE','PUT'])    
def new(request):
    if request.method == 'POST':
      try:
        Listas.objects.get(quando=request.data['lista_relacionada'],status='ativo')
        return Response(status=status.HTTP_400_BAD_REQUEST)
      except:
        serializer = ListasSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_200_OK)
        else:
          return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
      try:
        lista = Listas.objects.get(quando=request.data['lista_relacionada'],status='ativo')
        participacoes = Participacoes.objects.filter(lista_relacionada = request.data['lista_relacionada'],status='ativo').all()
        for item in participacoes:
            item.delete()
        lista.delete()
        return Response(status=status.HTTP_200_OK)
      except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
      try:
        lista_a_modificar = Listas.objects.get(quando=request.data['lista_relacionada'],status='ativo')
        serialize = ListasSerializer(lista_a_modificar,data=request.data)
        if serialize.is_valid():
          serialize.save()
          return Response(serialize.data,status=status.HTTP_200_OK)
        else:
          return Response(status=status.HTTP_404_NOT_FOUND)
      except:
          return Response(status=status.HTTP_404_NOT_FOUND)
    
      
@api_view(['GET'])    
def ver_listas_ativas(request):
  if request.method == 'GET':
    try:
      listas_ativas = Listas.objects.filter(status='ativo').all()
      serializer = ListasSerializer(listas_ativas,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)
    except :
      return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])    
def ver_listas(request):
  if request.method == 'GET':
    try:
      listas_ativas = Listas.objects.all()
      serializer = ListasSerializer(listas_ativas,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)
    except :
      return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST','DELETE'])    
def participar_lista(request):
  if request.method == 'POST':
    try:
      lista_a_se_modificar = Listas.objects.get(quando=request.data['lista_relacionada'],status='ativo').quando
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)
    try:
      participacao = Participacoes.objects.get(lista_relacionada=lista_a_se_modificar,status='ativo',participante=request.data['participante'])
      return Response(status=status.HTTP_400_BAD_REQUEST)    
    except:
      serializer = ParticipacoesSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
      else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
  if request.method == 'DELETE':
    try:
      cancelamento = Participacoes.objects.get(lista_relacionada=request.data['lista_relacionada'],participante=request.data['participante'])
      cancelamento.delete()
      return Response(status=status.HTTP_200_OK)
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])      
def participantes_lista(request):
  if request.method == 'GET':
    total_participantes_lista = Participacoes.objects.filter(lista_relacionada = request.data['lista_relacionada'],status='ativo').all()
    print(total_participantes_lista)
    if total_participantes_lista != None:
      return JsonResponse({"total":len(total_participantes_lista)})
    else:
      return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET']) 
def ver_participantes(request):
    if request.method == 'GET':
        participantes = Participacoes.objects.filter(lista_relacionada = request.data['lista_relacionada'],status='ativo').all()
        print([item.participante for item in participantes])
        return JsonResponse({"participantes":[item.participante for item in participantes]})
    
