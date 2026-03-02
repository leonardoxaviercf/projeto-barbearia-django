# Documentação Detalhada - Barbearia Xavier

## 1. Proposta do Sistema
O sistema da Barbearia Xavier é uma solução de agendamento e gestão voltada para barbearias que buscam profissionalizar o atendimento e fidelizar clientes através de uma interface moderna e notificações proativas.

## 2. Pontos Positivos e Diferenciais
* **Inteligência Temporal**: O sistema possui uma lógica de notificações na Home que adapta a linguagem conforme a proximidade do agendamento (Hoje, Amanhã ou Data Específica), reduzindo a taxa de absenteísmo.
* **Identidade Visual Coesa (Black & Gold)**: Diferente de sistemas que utilizam o padrão do Django Admin, este projeto possui todos os fluxos de usuário (login, cadastro, alteração de senha) estilizados com CSS personalizado.
* **Integridade via E-mail**: Utiliza o e-mail como chave mestra de relacionamento. Isso garante que, mesmo que o registro de Cliente e User sejam criados em momentos distintos, os agendamentos permaneçam vinculados ao proprietário legítimo.
* **Dashboard Financeiro**: O cliente visualiza o total gasto e o histórico, enquanto o gestor tem acesso a gráficos de demanda por serviço e agenda geral.

## 3. Disponibilidades e Funcionalidades
### Para o Cliente:
* Visualização de catálogo de serviços e preços em tempo real.
* Agendamento com escolha de barbeiro, data e múltiplos serviços simultâneos.
* Dashboard pessoal para acompanhamento e cancelamento de horários futuros.
* Lembrete automático de compromissos na página inicial.

### Para a Barbearia (Admin/Staff):
* Agenda Geral consolidada com visão diária e futura.
* Gráficos de desempenho (serviços mais pedidos).
* Gestão de usuários, clientes e barbeiros de forma independente.

## 4. Arquitetura Técnica
* **Backend**: Django 6.x.
* **Banco de Dados**: MySQL (Produção)
* **Frontend**: Django Template Language integrado com CSS3 e conceitos de UX Design.
* **Segurança**: Filtros em nível de banco de dados (`Q objects` e `request.user.email`) para isolamento de dados entre clientes.

## 5. Segurança e Isolamento de Dados
O sistema implementa uma camada de segurança no Backend para garantir que cada cliente acesse exclusivamente suas próprias informações. 

1. **Filtro por Identidade Única**: As consultas ao banco de dados (QuerySets) utilizam o e-mail do usuário autenticado (`request.user.email`) como chave de busca primária.
2. **Prevenção de Acesso Indevido**: Mesmo que um usuário tente acessar o Dashboard ou cancelar um agendamento via URL, o sistema valida se o registro pertence ao e-mail logado, retornando erro ou redirecionando caso haja divergência.
3. **Integridade Cross-Profile**: A lógica de filtragem foi projetada para unificar agendamentos realizados em diferentes momentos, desde que o e-mail de referência seja o mesmo, mantendo a consistência do histórico do cliente.