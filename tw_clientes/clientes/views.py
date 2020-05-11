from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClientForm
# Create your views here.

def listar_clientes(request):
    #método que retorna todos os clientes objects.all()
    clientes = Cliente.objects.all()
    #é dentro da variável 'clientes' que todos os clientes vai ser inseridos. Neste caso está dando o mesmo nome acima para facilitar.
    return render(request,'clientes/listar_clientes.html',{'clientes': clientes})

def inserir_cliente(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_clientes")
    else:
        form = ClientForm()
    return render(request, 'clientes/form_cliente.html', {'form':form})

def listar_cliente_id(request,id):
    cliente = Cliente.objects.get(id=id)
    return render(request,'clientes/listar_cliente.html', {'cliente': cliente})


def editar_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    # pega o formulário preenchido se o método por post, vazio se não for post e cria uma instancia do cliente
    form = ClientForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect("listar_clientes")
    # cria uma requisição, renderiza o template form_cliente e chama o formulário do cliente
    return render(request,'clientes/form_cliente.html', {'form': form})

def remover_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect("listar_clientes")
    return render(request,'clientes/confirma_exclusao.html', {'cliente': cliente})
