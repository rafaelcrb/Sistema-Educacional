from django.shortcuts import render, redirect
from .models import Aluno, Curso
from .forms import CadastroAluno, CadastroCurso

def pag_inicial(request):
    return render(request, 'escola/index.html')


def lista_alunos(request):
    alunos = Aluno.objects.all()
    context = {
        'alunos': alunos
    }
    return render(request, 'escola/lista_alunos.html', context)

def lista_cursos(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'escola/lista_cursos.html', context)

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = CadastroAluno(request.POST)
        if form.is_valid():
            aluno = form.save()  
            aluno.cursos.set(form.cleaned_data['cursos'])  # Associa os cursos selecionados
            return redirect('lista_alunos')  
    else:
        form = CadastroAluno()
    return render(request, 'escola/cadastro_aluno.html', {'form': form})

def cadastrar_curso(request):
    if request.method == 'POST':
        form = CadastroCurso(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('lista_cursos')  
    else:
        form = CadastroAluno()
    return render(request, 'escola/cadastro_curso.html', {'form': form})