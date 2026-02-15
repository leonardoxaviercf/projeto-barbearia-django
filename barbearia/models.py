from django.db import models

# Create your models here.

from django.db import models

class Cliente(models.Model):
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

class Agendamento(models.Model):
    # Relacionamentos 1:N conforme seu diagrama que está registrado na pasta components
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE, related_name='agendamentos')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agendamentos')
    data = models.DateTimeField()
    
    def __str__(self):
        return f"Agendamento {self.id} - {self.cliente.nome}"

class ItensAgendamento(models.Model):
    # Esta tabela faz a ligação N:N entre Agendamento e Servico
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE, related_name='itens')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    # Salvamos o preço pago no momento para histórico, caso o preço da tabela mude depois
    preco_pago = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.servico.nome} (Agendamento {self.agendamento.id})"