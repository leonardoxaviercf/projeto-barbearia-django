from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Cliente, Barbeiro, Servico, Agendamento, ItensAgendamento

# Configura a exibição dos itens dentro da tela de Agendamento
class ItensAgendamentoInline(admin.TabularInline):
    model = ItensAgendamento
    extra = 1 # Define quantos campos vazios aparecem por padrão
    fields = ['servico', 'preco_pago']

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'barbeiro', 'data')
    list_filter = ('data', 'barbeiro')
    inlines = [ItensAgendamentoInline] # Adiciona o "carrinho" aqui

# Registros simples para as outras tabelas
admin.site.register(Cliente)
admin.site.register(Barbeiro)
admin.site.register(Servico)