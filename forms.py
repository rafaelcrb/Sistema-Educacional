from django import forms
from .models import Aluno, Curso

class CadastroAluno(forms.ModelForm):
    cursos = forms.ModelMultipleChoiceField(
        queryset=Curso.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Cursos"
    )

    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'email', 'cursos']

class CadastroCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descricao']