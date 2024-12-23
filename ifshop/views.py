from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Camiseta, Pedido
from .forms import CamisetaForm, PedidoForm, FiltroProdutoForm, CadastroUsuarioForm, LoginUsuarioForm

def index(request):
    form = FiltroProdutoForm(request.GET) 
    camisetas =Camiseta.objects.all()

    if form.is_valid():
        turnos = form.cleaned_data.get('turnos')
        cursos = form.cleaned_data.get('cursos')

        if turnos:  
            camisetas = camisetas.filter(turnos=turnos)

        if cursos:  
            camisetas = camisetas.filter(cursos=cursos)

    context = {
        'form': form,
        'camisetas': camisetas,
    }
    return render(request, 'index.html', context )

####################################################################################################

def vendedor(user):
    return user.vendedor

def login_view(request):
    if request.method == 'POST':
        form = LoginUsuarioForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  
            login(request, user)
            return redirect('perfil')  
    else:
        form = LoginUsuarioForm()
    return render(request, 'login.html', {'form': form})

def logout_usuario(request):
    logout(request) 
    return redirect('login')

####################################################################################################

@login_required
def perfil(request):
    if request.user.is_authenticated:
        camisetas = Camiseta.objects.filter(vendedor=request.user)  
    else:
        camisetas = [] 

    return render(request, 'perfil.html', {'camisetas': camisetas})

####################################################################################################

def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('index') 
    else:
        form = CadastroUsuarioForm()
    return render(request, 'cadastro.html', {'form': form})

####################################################################################################

def carrinho(request):
    pedidos = Pedido.objects.all()
    if request.method == "POST" and 'deletar' in request.POST:
        pedido_id = request.POST.get('pedido_id')
        pedido = Pedido.objects.get(id=pedido_id)
        pedido.delete()
        return redirect('carrinho')
    
    return render(request, "carrinho.html", {'pedidos': pedidos})

####################################################################################################

def camiseta(request, camiseta_id):
    camiseta = Camiseta.objects.get(id=camiseta_id)
    
    tamanhos_opcoes = [t.strip() for t in camiseta.tamanhos.split(',')]
    estilos_opcoes = [e.strip() for e in camiseta.estilos.split(',')]

    if request.method == 'POST':
        form = PedidoForm(request.POST, tamanhos_opcoes=tamanhos_opcoes, estilos_opcoes=estilos_opcoes)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.camiseta = camiseta
            pedido.usuario = request.user
            pedido.save()
            return redirect('carrinho')
    else:
        form = PedidoForm(tamanhos_opcoes=tamanhos_opcoes, estilos_opcoes=estilos_opcoes)

    return render(request, 'camiseta.html', {'camiseta': camiseta, 'form': form})

####################################################################################################

@login_required
@user_passes_test(vendedor)
def adicionar_pro(request):
    if request.method == 'POST':
        form = CamisetaForm(request.POST, request.FILES)

        if form.is_valid():
            camiseta = form.save(commit=False)
            camiseta.vendedor = request.user
            camiseta.tamanhos = ', '.join(form.cleaned_data['tamanhos'])
            camiseta.estilos = ', '.join(form.cleaned_data['estilos'])
            camiseta.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = CamisetaForm()
    return render(request, 'adicionar_pro.html', {'form': form})

####################################################################################################

@login_required
@user_passes_test(vendedor)
def gerenciar_pro(request):
    if request.user.is_authenticated:
        camisetas = Camiseta.objects.filter(vendedor=request.user) 
        if request.method == "POST" and 'deletar' in request.POST:
            camiseta_id = request.POST.get('camiseta_id')
            camiseta = camiseta.objects.get(id=camiseta_id)
            camiseta.delete()
            return redirect('gerenciar_pro')
    else:
        camisetas = []
    return render(request, 'gerenciar_pro.html', {'camisetas': camisetas})