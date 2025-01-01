from django.contrib import admin
from django.urls import path

from . import views,views_lists

urlpatterns = [
  path('',views.consultar_clientes,name='consultar_clientes'),
  path("usuario/manipular/<str:user>/",views.manipular_usuario),
  path("<str:site>/",views.consultar_clientes_por_site),
  path('usuario/criacao/',views.criar_usuario),
  path('usuario/acesso/',views.acessar),
  path('listas/listasativas/',views_lists.ver_listas_ativas),
  path('new/lista/',views_lists.new),
  path('listas/participacao/',views_lists.participar_lista),
  path('lista/ativa/totalparticipantes/',views_lists.participantes_lista),
  path('lista/participantes/',views_lists.ver_participantes)
]
