# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, redirect
import datetime

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import JsonResponse
from django.core.mail import send_mail, BadHeaderError
from django.core import mail
from core.models import Comentario, Eventos


def index(request):
    return render(request, 'index.html')

def handler404(request, exception):
    return render(request, '404.html')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

def cadastro(request):
    return render(request, 'cadastro.html')

def submit_cadastro(request):
    if request.POST:
        userName = request.POST.get('username', None)
        pnome = request.POST.get('pnome')
        unome = request.POST.get('unome')
        senha = request.POST.get('password', None)
        userMail = request.POST.get('e-mail', None)
        if userName and senha and userMail:
            usuario = authenticate(username=userName, password=senha)
            if usuario is not None:
                messages.error(request, "Usuário existente.")
            else:
                userCriar = User.objects.create_user(userName, userMail, senha)
                userCriar.first_name = pnome
                userCriar.last_nome = unome
                userCriar.groups.set(['grupo_usuario'])
                return redirect('/')
        else:
            messages.error(request, "Campos inválidos")
    return redirect('/')

def about_us(request):
    return render(request, 'about.html')

def photos(request):
    return render(request, 'photos.html')

def parceiros(request):
    return render(request, 'parceiros.html')

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')

def submit_contact(request):
    if request.POST:
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        empresa = request.POST.get('empresa', None)
        message = request.POST.get('message', None)
        mensagem = 'Nome: '+ name + '\n Empresa: ' + empresa + '\n E-mail: ' + email + '\n Mensagem:\n' + message
        if mensagem and email:
            with mail.get_connection() as connection:
                mail.EmailMessage('Contato via site', mensagem, email, ['turismojoinville.g7@gmail.com'],connection=connection,).send()
                return render(request, 'obrigado.html')
        else:
            messages.error(request, "Campos inválidos")
    return redirect('/')

def eventos(request):
    descricao = Eventos.objects.all().filter(data_evento__gte=datetime.now())
    dados = {'descricao': descricao}
    return render(request, 'eventos.html', dados)

def moinho(request):
    avaliacao = Comentario.objects.all().filter(local='moinho').order_by('-id')[:5]
    dados = {'avaliacao': avaliacao}
    return render(request, 'moinho.html', dados)

def serra(request):
    avaliacao = Comentario.objects.all().filter(local='serra').order_by('-id')[:5]
    dados = {'avaliacao': avaliacao}
    return render(request, 'serra.html', dados)

def rpalmeiras(request):
    avaliacao = Comentario.objects.all().filter(local='rpalmeiras').order_by('-id')[:5]
    dados = {'avaliacao': avaliacao}
    return render(request, 'rpalmeiras.html', dados)

def estradabonita(request):
    avaliacao = Comentario.objects.all().filter(local='estradabonita').order_by('-id')[:5]
    dados = {'avaliacao': avaliacao}
    return render(request, 'estradabonita.html', dados)

def mercado(request):
    avaliacao = Comentario.objects.all().filter(local='mercado').order_by('-id')[:5]
    dados = {'avaliacao': avaliacao}
    return render(request, 'mercado.html', dados)

def mirante(request):
    avaliacao = Comentario.objects.all().filter(local='mirante').order_by('-id')[:5]
    dados = {'avaliacao': avaliacao}
    return render(request, 'mirante.html', dados)

def morrofinder(request):
    avaliacao = Comentario.objects.all().filter(local='morrofinder').order_by('-id')[:5]
    dados = {'avaliacao': avaliacao}
    return render(request, 'morrofinder.html', dados)

def castelobugres(request):
    avaliacao = Comentario.objects.all().filter(local='castelobugres').order_by('-id')[:5]
    dados = {'avaliacao': avaliacao}
    return render(request, 'castelobugres.html', dados)

def parquemar(request):
    avaliacao = Comentario.objects.all().filter(local='parquemar').order_by('-id')[:5]
    dados = {'avaliacao': avaliacao}
    return render(request, 'parquemar.html', dados)

def zoobotanico(request):
    avaliacao = Comentario.objects.all().filter(local='zoobotanico').order_by('-id')[:5]
    dados = {'avaliacao': avaliacao}
    return render(request, 'zoobotanico.html', dados)

def estacao(request):
    avaliacao = Comentario.objects.all().filter(local='estacao').order_by('-id')[:5]
    dados = {'avaliacao': avaliacao}
    return render(request, 'estacao.html', dados)

def submit_comentario(request):
    if request.POST:
        usuario = request.user
        local = request.POST.get('local')
        texto = request.POST.get('message')
        if usuario and texto and local:
            Comentario.objects.create(local=local,avaliacao=texto,usuario=usuario)
            return redirect('/'+local)
        else:
            messages.error(request, "Comentário não enviado!")
            return redirect('/')