from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import Cliente, Servico, agendamento
from django.contrib import messages
from datetime import datetime, date


def agendar(request):
    servicos = Servico.objects.all()
    hoje = date.today().isoformat()

    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        servico_ids = request.POST.getlist('servicos')
        data_str = request.POST['data']
        hora_str = request.POST['hora']

        data_agendamento = datetime.strptime(data_str, '%Y-%m-%d').date()
        hora_agendamento = datetime.strptime(hora_str, '%H:%M').time()

        # Verificar se hora termina em :00
        if hora_agendamento.minute != 0:
            messages.error(request, 'Os agendamentos só podem ser feitos de hora em hora (ex: 13:00, 14:00).')
            return render(request, 'agendamentos/agendar.html', {'servicos': servicos, 'hoje': hoje})

        # Verificar se data/hora não é passada
        agora = datetime.now()
        agendamento_datetime = datetime.combine(data_agendamento, hora_agendamento)
        if agendamento_datetime < agora:
            messages.error(request, 'Você não pode agendar para uma data e hora passada.')
            return render(request, 'agendamentos/agendar.html', {'servicos': servicos, 'hoje': hoje})

        # Verificar se já existe agendamento no mesmo dia e hora
        existe = agendamento.objects.filter(data=data_agendamento, hora=hora_agendamento).exists()
        if existe:
            messages.error(request, 'Este horário já está ocupado. Por favor, escolha outro.')
            return render(request, 'agendamentos/agendar.html', {'servicos': servicos, 'hoje': hoje})

        # Criar ou obter cliente para evitar duplicatas
        cliente, created = Cliente.objects.get_or_create(nome=nome, telefone=telefone)

        # Criar agendamento
        novo_agendamento = agendamento.objects.create(cliente=cliente, data=data_agendamento, hora=hora_agendamento)
        novo_agendamento.servicos.set(servico_ids)

        messages.success(request, 'Agendamento realizado com sucesso!')
        return redirect('agendar')

    return render(request, 'agendamentos/agendar.html', {'servicos': servicos, 'hoje': hoje})


@login_required(login_url='login')
def listar_agendamentos(request):
    agendamentos = agendamento.objects.all().order_by('-data', '-hora')
    return render(request, 'agendamentos/listar_agendamentos.html', {'agendamentos': agendamentos})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            return redirect('listar_agendamentos')
        else:
            return render(request, 'agendamentos/login.html', {'erro': 'Usuário ou senha inválidos'})
    return render(request, 'agendamentos/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
