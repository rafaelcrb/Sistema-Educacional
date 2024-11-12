from django.urls import path
from . import views

urlpatterns = [
    path('', views.pag_inicial, name='pag_inicial'),
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('alunos/cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('cursos/cadastrar/', views.cadastrar_curso, name='cadastrar_curso'),
]
