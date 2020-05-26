from django.urls import path
from .views import *

urlpatterns = [
    #método listar vai ser após o clientes, chama a view listar_clientes e o name é para ser mais fácil de ser localizado
    path('listar', listar_clientes, name='listar_clientes'),
    path('cadastrar', inserir_cliente, name='cadastrar_cliente'),
    path('listar/<int:id>',listar_cliente_id, name = 'listar_cliente_id'),
    path('editar/<int:id>', editar_cliente, name='editar_cliente'),
    path('remover/<int:id>', remover_cliente, name='remover_cliente'),
    path('cadastrar/endereco', inserir_endereco, name='cadastrar_endereco'),
    path('listar/endereco', listar_enderecos, name='listar_enderecos')
]
