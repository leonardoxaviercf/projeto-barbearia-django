from django.db import models
from django.conf import settings

# Create your models here.
class Cliente(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Barbeiro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=50)
    preco_tabela = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
    
# Relacionamentos 1:N
class Agendamento(models.Model):
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE, related_name='agendamentos')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agendamentos')
    data = models.DateTimeField()
    
    def __str__(self):
        return f"Agendamento {self.id} - {self.cliente.nome}"

# Esta tabela faz a ligacao N:N entre Agendamento e Servico
class ItensAgendamento(models.Model):
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE, related_name='itens')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    # Salva o preco pago no atendimento caso o preco sofra alteracoes com o tempo
    preco_pago = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.servico.nome} (Agendamento {self.agendamento.id})"