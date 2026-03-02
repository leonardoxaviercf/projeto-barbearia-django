from django.shortcuts import render, redirect, get_object_or_404
from .models import Servico, Cliente, Agendamento
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import AgendamentoForm, ItensAgendamentoFormSet
import json
from datetime import datetime
from django.db.models import Sum
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count

def home(request):
    notificacao = None
    agora = timezone.now()
    hoje = agora.date()
    amanha = hoje + timezone.timedelta(days=1)
    
    if request.user.is_authenticated:
        proximo_agendamento = Agendamento.objects.filter(
            cliente__email=request.user.email,
            data__gte=agora 
        ).select_related('barbeiro').order_by('data').first()
        
        if proximo_agendamento:
            notificacao = proximo_agendamento

    return render(request, 'barbearia/home.html', {
        'notificacao': notificacao,
        'hoje': hoje,
        'amanha': amanha
    })

def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'barbearia/servicos.html', {'servicos': servicos})

@login_required
def criar_agendamento(request):
    storage = messages.get_messages(request)
    storage.used = True
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        formset = ItensAgendamentoFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            servicos_preenchidos = [
                f for f in formset.cleaned_data 
                if f.get('servico') and not f.get('DELETE')
            ]
            
            if not servicos_preenchidos:
                form.add_error(None, "Você precisa adicionar pelo menos um serviço.") 
            else:
                cliente, created = Cliente.objects.get_or_create(
                    email=request.user.email, # Busca pelo e-mail que é único
                    defaults={
                        'usuario': request.user,
                        'nome': request.user.first_name or request.user.username,
                    }
                )
                
                agendamento = form.save(commit=False)
                agendamento.cliente = cliente 
                
                dia = form.cleaned_data['dia']
                hora = form.cleaned_data['hora']
                data_completa_str = f"{dia} {hora}"
                agendamento.data = datetime.strptime(data_completa_str, '%Y-%m-%d %H:%M')
                
                agendamento.save()
                
                instances = formset.save(commit=False)
                for instance in instances:
                    if instance not in formset.deleted_objects:
                        if instance.preco_pago:
                            valor_limpo = str(instance.preco_pago).replace(',', '.')
                            instance.preco_pago = float(valor_limpo)
                        instance.agendamento = agendamento 
                        instance.save()
                
                return render(request, 'barbearia/sucesso.html')
    else:
        form = AgendamentoForm()
        formset = ItensAgendamentoFormSet()
    
    servicos_dados = {s.id: float(s.preco_tabela) for s in Servico.objects.all()}

    return render(request, 'barbearia/agendar.html', {
        'form': form, 
        'formset': formset,
        'servicos_json': json.dumps(servicos_dados)
    })

@login_required
def dashboard_cliente(request):
    agendamentos = Agendamento.objects.filter(
        cliente__email=request.user.email
    ).select_related('barbeiro').annotate(
        total=Sum('itens__preco_pago') 
    ).order_by('-data')

    return render(request, 'barbearia/dashboard.html', {
        'agendamentos': agendamentos,
        'now': timezone.now()
    })

@login_required
def cancelar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id, cliente__email=request.user.email)
    
    if agendamento.data > timezone.now():
        agendamento.delete()
        messages.success(request, "Agendamento cancelado com sucesso.")
    else:
        messages.error(request, "Não é possível cancelar agendamentos passados.")
        
    return redirect('dashboard_cliente')

@staff_member_required
def agenda_geral(request):
    hoje = timezone.now().date()
    agendamentos = Agendamento.objects.filter(data__date__gte=hoje).select_related('barbeiro', 'cliente').annotate(total=Sum('itens__preco_pago')).order_by('data')

    dados_grafico = Servico.objects.annotate(
        qtd_pedidos=Count('itensagendamento')
    ).values('nome', 'qtd_pedidos')

    return render(request, 'barbearia/agenda_geral.html', {
        'agendamentos': agendamentos,
        'hoje': hoje,
        'labels': json.dumps([item['nome'] for item in dados_grafico]),
        'valores': json.dumps([item['qtd_pedidos'] for item in dados_grafico]),
    })

@login_required
def perfil_usuario(request):
    cliente = Cliente.objects.filter(usuario=request.user).first()
    
    return render(request, 'barbearia/perfil.html', {
        'cliente': cliente
    })
