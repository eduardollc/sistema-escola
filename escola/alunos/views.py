from django.shortcuts import render
from .models import Aluno
from django.db.models import Q

# Create your views here.

def cadastrar(request):
    if request.method == 'POST':
        matricula = request.POST['matricula']
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        idade = request.POST['idade']
        email = request.POST['email']
        telefone = request.POST['telefone']
        endereco =  request.POST['endereco']

        aluno = Aluno(
            matricula=matricula,
            nome=nome,
            cpf=cpf,
            idade=idade,
            email=email,
            telefone=telefone,
            endereco=endereco
        )

        aluno.save()

    return render(request, 'alunos/cadastrar.html')

def lista(request):
    alunos = Aluno.objects.all()
    return render(
        request,
        "alunos/lista.html",
        {"alunos": alunos}
    )

def pesquisar(request):
    termo = request.GET.get('q', '')

    alunos = []

    if termo:
        alunos = Aluno.objects.filter(
            Q(nome__icontains=termo) |
            Q(matricula__icontains=termo)
        )

    return render (request, 'alunos/pesquisar.html', {
        'alunos':alunos,
        'termo':termo
    })
