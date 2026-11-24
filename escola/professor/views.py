from django.shortcuts import render
from .models import Professor

# Create your views here.
def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        email = request.POST['email']
        telefone = request.POST['telefone']

        professor = Professor(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone
        )

        professor.save()

    return render(request, 'professores/cadastrar.html')

def lista(request):
    professor = Professor.objects.all()
    return render(
        request, 
        "professores/lista.html",
        {"professor":professor}

    )