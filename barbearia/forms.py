from django import forms
from .models import Agendamento, ItensAgendamento
from datetime import datetime
from django.utils import timezone

class AgendamentoForm(forms.ModelForm):
    HORARIOS_ATENDIMENTO = [
        (None, 'Escolha o horário'),
        ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'),
        ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'),
        ('17:00', '17:00'), ('18:00', '18:00'),
    ]
    
    dia = forms.DateField(
        label="Data",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input'})
    )

    hora = forms.ChoiceField(
        label="Horário",
        choices=HORARIOS_ATENDIMENTO,
        widget=forms.Select(attrs={'class': 'form-input'})
    )

    class Meta:
        model = Agendamento
        fields = ['barbeiro', 'dia', 'hora']

    def clean(self):
        cleaned_data = super().clean()
        barbeiro = cleaned_data.get('barbeiro')
        dia = cleaned_data.get('dia')
        hora_str = cleaned_data.get('hora')

        if barbeiro and dia and hora_str:
            data_agendamento = datetime.combine(dia, datetime.strptime(hora_str, '%H:%M').time())
            
            if timezone.is_aware(timezone.now()):
                data_agendamento = timezone.make_aware(data_agendamento)

            conflito = Agendamento.objects.filter(
                barbeiro=barbeiro,
                data=data_agendamento
            ).exists()

            if conflito:
                self.add_error('hora', f"O barbeiro {barbeiro} já possui um agendamento para este dia às {hora_str}.")

        return cleaned_data
class ItensAgendamentoForm(forms.ModelForm):
    class Meta:
        model = ItensAgendamento
        fields = ['servico', 'preco_pago']
        widgets = {
            'preco_pago': forms.TextInput(attrs={
                'readonly': 'readonly',
                'class': 'readonly-input',
                'tabindex': '-1'
            }),
        }


ItensAgendamentoFormSet = forms.inlineformset_factory(
    Agendamento, 
    ItensAgendamento,
    form=ItensAgendamentoForm, # Conecta com a classe acima
    extra=1,
    can_delete=True
)