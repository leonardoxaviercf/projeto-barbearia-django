from django.shortcuts import render
from .models import Servico

# Create your views here.


def home(request):
    return render(request, 'home.html')

def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos.html', {'servicos': servicos})