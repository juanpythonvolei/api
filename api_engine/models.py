from django.db import models

# Create your models here.
class Usuarios(models.Model):
  
  nome_site = models.CharField(max_length=500,default='',primary_key=True,unique=True)
  nome = models.CharField(max_length=500,default='')
  senha = models.IntegerField(default=0)

  
class Listas(models.Model):
  
  quando = models.CharField(max_length=500,default='',primary_key=True,unique=True)
  criador = models.CharField(max_length=500,default='')
  qtd_participantes = models.IntegerField(default=0)
  status = models.CharField(max_length=500,default='')
  local = models.CharField(max_length=500,default='')

class Participacoes(models.Model):
  
  participante =  models.CharField(max_length=500,default='',unique=True,primary_key=True)
  lista_relacionada = models.CharField(max_length=500,default='')
  status = models.CharField(max_length=500,default='')
