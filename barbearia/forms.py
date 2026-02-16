from django import forms
from .models import Agendamento, ItensAgendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['barbeiro', 'data']
        widgets = {
            'data': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input'}),
        }

# O Inline Formset permite adicionar vários itens em um único formulário
ItensAgendamentoFormSet = forms.inlineformset_factory(
    Agendamento, 
    ItensAgendamento,
    fields=['servico', 'preco_pago'],
    extra=3,
    can_delete=True
)