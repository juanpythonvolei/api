from rest_framework import serializers
from .models import *

class UsuariosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuarios
    fields = '__all__'
class ListasSerializer(serializers.ModelSerializer):
  class Meta:
    model = Listas
    fields = '__all__'    

class ParticipacoesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Participacoes
    fields = '__all__'     
