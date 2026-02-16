from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicos/', views.lista_servicos, name='lista_servicos'),
    path('agendar/', views.criar_agendamento, name='criar_agendamento'),
]