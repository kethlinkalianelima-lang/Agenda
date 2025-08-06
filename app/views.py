from django.shortcuts import render, redirect
from app.models import Agenda

# Create your views here.



def novo_cntt(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        Agenda.novo(nome,telefone)
        return render (request, 'add_cntt.html')
    
    return render (request, 'add_cntt.html')


def index(request):
    contatos = Agenda.listar()
    return  render (request, 'index.html', {'contatos':contatos})



def deletar(request, id):
    d = Agenda.deletar(id=id)
    return redirect ('index')
    