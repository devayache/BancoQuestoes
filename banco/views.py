from django.shortcuts import render, redirect
from .models import Questoes
# Create your views here.

def index(request):
    return render(request, 'index.html')

def cadastrar_questoes(request):
    if request.method == 'GET':
        return render(request,'cadQuestoes.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        assunto = request.POST.get('assunto')
        area = request.POST.get('area')
        texto = request.POST.get('texto')
        return render(request,'cadQuestoes.html')

def tabela(request):
    questao = Questoes.objects.all()
    return render(request, 'tabela.html', {'questao':questao})


