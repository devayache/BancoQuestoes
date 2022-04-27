from django.shortcuts import render, redirect
from .models import Questoes
from .forms import QuestoesForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def cadastrar_questoes(request):
    if request.method == 'GET':
        return render(request,'cadQuestoes.html')
    elif request.method == 'POST':
        form = QuestoesForm(request.POST)
        if form.is_valid():
            nova_questoes = form.save()
        return redirect('tabela')

def tabela(request):
    questao = Questoes.objects.all()
    return render(request, 'tabela.html', {'questao':questao})


