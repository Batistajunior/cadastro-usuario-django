# app_cad_usuarios/views.py
from django.shortcuts import render
from .models import Usuario  # Importe a classe Usuario do arquivo models.py

def home(request):
    return render(request, 'user/home.html')

def usuarios(request):
    if request.method == 'POST':
        # Salvando os dados na tabela de dados.
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade') 
        novo_usuario.save()

    # Exibir todos os usuários já cadastrados em uma nova página 
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a página de listagem de usuários
    return render(request, 'user/usuarios.html', usuarios)
