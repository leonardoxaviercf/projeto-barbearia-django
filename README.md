# 🪒 Barbearia Xavier - Sistema de Agendamento

Este projeto é um MVP (Minimum Viable Product) desenvolvido para a gestão de agendamentos da **Barbearia Xavier**, localizada em Ceará-Mirim/RN. O foco do sistema é automatizar o fluxo de marcação de horários, integrando uma interface moderna com uma estrutura robusta de backend.

## 🎯 Funcionalidades
* **Autenticação de Usuários**: Sistema completo de cadastro, login e redefinição de senha.
* **Agendamento Dinâmico**: Carrinho de serviços com cálculo de total em tempo real (JavaScript + Django Formsets).
* **Dashboard do Cliente**: Visualização e cancelamento de agendamentos ativos.
* **Agenda Geral (Admin)**: Painel com gráficos (Chart.js) para análise de serviços mais procurados.
* **Notificações**: Lembretes inteligentes na Home baseados na data do agendamento.

## 💻 Stack Técnica
* **Linguagem**: Python 3.12
* **Framework**: Django (MTV Architecture)
* **Frontend**: HTML5, CSS3 (Arquitetura Utilitária/Dry CSS) e JavaScript.
* **Banco de Dados**: MySQL
* **Gráficos**: Chart.js para insights de negócio.

## 🏗️ Padrões de Projeto Aplicados
* **Refatoração de CSS**: Migração de estilos inline para um sistema de classes utilitárias, aumentando a manutenibilidade do código.
* **Django Templates**: Uso extensivo de `template inheritance` para reaproveitamento de componentes como `base.html`.
* **Modelos Relacionais**: Estrutura otimizada entre `Cliente`, `Barbeiro`, `Serviço` e `Agendamento`.

## 🛠️ Instruções de Instalação

1. **Clonar o repositório:**
   ```bash
   git clone (https://github.com/leonardoxaviercf/projeto-barbearia-django.git)
   cd barbearia-xavier
   ```

2. **Configurar ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    ```

3. **Instalar dependências:**
    ```bash
    pip install django mysqlclient
    ```

4. **Configurações iniciais:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

## 👨‍💻 Autor

**Leonardo Xavier Cruz Filho**

* 🎓 **Graduando em Tecnologia da Informação (BTI)** - IMD/UFRN
* 📜 **Técnico em Informática** - IFRN
* 🎯 **Foco**: Desenvolvimento Backend (Python/Django/Java)