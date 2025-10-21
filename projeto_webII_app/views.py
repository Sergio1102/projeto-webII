from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Evento, Local, Palestrante, CategoriaEvento, Inscricao
from .forms import FormularioEvento, FormularioLocal, FormularioPalestrante, FormularioCatEvento

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def listarEventos(request):
    lista_eventos = Evento.objects.all().order_by('-data_hora')
    
    paginator = Paginator(lista_eventos, 5)
    num_pagina = request.GET.get('page')
    obj_pagina = paginator.get_page(num_pagina)
    
    return render(request, 'app/listarEventos.html', {'obj_pagina': obj_pagina})

def detalharEvento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    inscrito = False
    if request.user.is_authenticated:
        inscrito = Inscricao.objects.filter(participante=request.user, evento=evento).exists()
    return render(request, 'app/detalharEvento.html', {'evento': evento, 'inscrito': inscrito})

@login_required(login_url='/login/')
def criarEvento(request):
    if request.method == 'POST':
        form = FormularioEvento(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listarEventos')
    else:
        form = FormularioEvento()
    return render(request, 'app/formularioEvento.html', {'form': form, 'tipo': 'Cadastrar Evento'})

@login_required(login_url='/login/')
def atualizarEvento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    form = FormularioEvento(request.POST or None, request.FILES or None, instance=evento)
    
    if form.is_valid():
        form.save()
        return redirect('listarEventos')
        
    return render(request, 'app/formularioEvento.html', {'form': form, 'tipo': 'Editar Evento'})

@login_required(login_url='/login/')
def apagarEvento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('listarEventos')
    return render(request, 'app/apagarEvento.html', {'objeto': evento, 'tipo': 'Evento'})


def listarLocais(request):
    lista_locais = Local.objects.all().order_by('nome')
    
    paginator = Paginator(lista_locais, 5)
    num_pagina = request.GET.get('page')
    obj_pagina = paginator.get_page(num_pagina)
    
    return render(request, 'app/listarLocais.html', {'obj_pagina': obj_pagina})

@login_required(login_url='/login/')
def criarLocal(request):
    if request.method == 'POST':
        form = FormularioLocal(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarLocais')
    else:
        form = FormularioLocal()
    return render(request, 'app/formularioGenerico.html', {'form': form, 'tipo': 'Cadastrar Local'})

@login_required(login_url='/login/')
def atualizarLocal(request, id):
    local = get_object_or_404(Local, pk=id)
    form = FormularioLocal(request.POST or None, instance=local)
    
    if form.is_valid():
        form.save()
        return redirect('listarLocais')
        
    return render(request, 'app/formularioGenerico.html', {'form': form, 'tipo': 'Editar Local'})

@login_required(login_url='/login/')
def apagarLocal(request, id):
    local = get_object_or_404(Local, pk=id)
    if request.method == 'POST':
        local.delete()
        return redirect('listarLocais')
    return render(request, 'app/apagarGenerico.html', {'objeto': local, 'tipo': 'Local'})


def listarPalestrantes(request):
    lista_palestrantes = Palestrante.objects.all().order_by('nome')
    
    paginator = Paginator(lista_palestrantes, 5)
    num_pagina = request.GET.get('page')
    obj_pagina = paginator.get_page(num_pagina)
    
    return render(request, 'app/listarPalestrantes.html', {'obj_pagina': obj_pagina})

@login_required(login_url='/login/')
def criarPalestrante(request):
    if request.method == 'POST':
        form = FormularioPalestrante(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listarPalestrantes')
    else:
        form = FormularioPalestrante()
    return render(request, 'app/formularioGenerico.html', {'form': form, 'tipo': 'Cadastrar Palestrante'})

@login_required(login_url='/login/')
def atualizarPalestrante(request, id):
    palestrante = get_object_or_404(Palestrante, pk=id)
    form = FormularioPalestrante(request.POST or None, request.FILES or None, instance=palestrante)
    
    if form.is_valid():
        form.save()
        return redirect('listarPalestrantes')
        
    return render(request, 'app/formularioGenerico.html', {'form': form, 'tipo': 'Editar Palestrante'})

@login_required(login_url='/login/')
def apagarPalestrante(request, id):
    palestrante = get_object_or_404(Palestrante, pk=id)
    if request.method == 'POST':
        palestrante.delete()
        return redirect('listarPalestrantes')
    return render(request, 'app/apagarGenerico.html', {'objeto': palestrante, 'tipo': 'Palestrante'})


def listarCatEventos(request):
    lista_categorias = CategoriaEvento.objects.all().order_by('nome')
    
    paginator = Paginator(lista_categorias, 5)
    num_pagina = request.GET.get('page')
    obj_pagina = paginator.get_page(num_pagina)
    
    return render(request, 'app/listarCatEventos.html', {'obj_pagina': obj_pagina})

@login_required(login_url='/login/')
def criarCatEvento(request):
    if request.method == 'POST':
        form = FormularioCatEvento(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarCatEventos')
    else:
        form = FormularioCatEvento()
    return render(request, 'app/formularioGenerico.html', {'form': form, 'tipo': 'Cadastrar Categoria'})

@login_required(login_url='/login/')
def atualizarCatEvento(request, id):
    categoria = get_object_or_404(CategoriaEvento, pk=id)
    form = FormularioCatEvento(request.POST or None, instance=categoria)
    
    if form.is_valid():
        form.save()
        return redirect('listarCatEventos')
        
    return render(request, 'app/formularioGenerico.html', {'form': form, 'tipo': 'Editar Categoria'})

@login_required(login_url='/login/')
def apagarCatEvento(request, id):
    categoria = get_object_or_404(CategoriaEvento, pk=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listarCatEventos')
    return render(request, 'app/apagarGenerico.html', {'objeto': categoria, 'tipo': 'Categoria'})

@login_required(login_url='/login/')
def inscrever_evento(request, id):
    if request.method == 'POST':
        evento = get_object_or_404(Evento, pk=id)
        Inscricao.objects.get_or_create(
            participante=request.user,
            evento=evento
        )
        
        return render(request, 'app/partials/_botao_inscrito.html')
    
    return redirect('detalharEvento', id=id)