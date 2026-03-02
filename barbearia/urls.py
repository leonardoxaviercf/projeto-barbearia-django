from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicos/', views.lista_servicos, name='lista_servicos'),
    path('agendar/', views.criar_agendamento, name='criar_agendamento'),
    path('dashboard/', views.dashboard_cliente, name='dashboard_cliente'),
    path('cancelar/<int:agendamento_id>/', views.cancelar_agendamento, name='cancelar_agendamento'),
    path('gestao/agenda/', views.agenda_geral, name='agenda_geral'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
]