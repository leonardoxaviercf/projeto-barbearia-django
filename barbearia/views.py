from django.shortcuts import render, redirect
from .models import Servico
from django.contrib.auth.decorators import login_required
from .forms import AgendamentoForm, ItensAgendamentoFormSet
from .models import Cliente

# Create your views here.


def home(request):
    return render(request, 'home.html')

def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos.html', {'servicos': servicos})

@login_required
def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        formset = ItensAgendamentoFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            cliente, created = Cliente.objects.get_or_create(
                email=request.user.email,
                defaults={'nome': request.user.username}
            )
            
            agendamento = form.save(commit=False)
            agendamento.cliente = cliente # Vincula o cliente logado
            agendamento.save()
            
            formset.instance = agendamento
            formset.save()
            
            return redirect('home')
    else:
        form = AgendamentoForm()
        formset = ItensAgendamentoFormSet()
    
    return render(request, 'agendar.html', {'form': form, 'formset': formset})