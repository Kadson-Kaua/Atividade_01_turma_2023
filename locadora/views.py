from django.shortcuts import render
from .models import locacao, filme
# Create your views here.
def index(request):
    return render(request, 'locadora/index.html')

def lista_locacao(request):
    lista = locacao.objects.all() #pegando dados do banco.
    context={'locacoes': lista} #preparando os dados para o .html
    return render(request,'locadora/lista_locacao.html',context)

def lista_filmes(request):
    lista = filme.objects.all() #pegando dados do banco.
    context={'filmes': lista} #preparando os dados para o .html
    return render(request,'locadora/lista_filmes.html',context)