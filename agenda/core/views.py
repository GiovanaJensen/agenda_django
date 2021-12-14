from django.shortcuts import render,redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

#def index(request):
    #return redirect("agenda/")

def login_user(request):
    return render(request,"login.html")

def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return redirect("/")

def logout_user(request):
    logout(request)
    return redirect("/")

@login_required(login_url="/login/")
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    #evento = Evento.objects.all()
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)

@login_required(login_url="/login/")
def evento(request):
    return render(request, "evento.html")

@login_required(login_url="/login/")
def evento_submit(request):
    if request.POST:
        nm_evento = request.POST.get("titulo")
        dt_evento = request.POST.get("data_evento")
        descricao = request.POST.get("descricao")
        usuario = request.user
        Evento.objects.create(titulo=nm_evento, dt_evento=dt_evento, descricao=descricao, usuario=usuario)
    return redirect('/')