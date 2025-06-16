# Documentação Técnica - Sistema Educacional

## 1. Visão Geral

O Sistema Educacional é uma aplicação web desenvolvida em Django, projetada para gerenciar informações de alunos e cursos. Ele oferece funcionalidades básicas para cadastro, listagem e gerenciamento de dados educacionais.

## 2. Estrutura do Projeto

A estrutura do projeto segue a convenção de aplicações Django, com módulos bem definidos para cada parte da aplicação:

```
Sistema-Educacional/
├── __init__.py
├── admin.py                    # Configurações do painel administrativo do Django
├── forms.py                    # Definições de formulários
├── models/                     # Definições dos modelos de dados
│   ├── __init__.py
│   ├── aluno.py                # Modelo para Aluno
│   └── curso.py                # Modelo para Curso
├── migrations/                 # Migrações do banco de dados
│   ├── 0001_initial.py
│   └── __init__.py
├── templates/                  # Modelos HTML para renderização das páginas
│   └── escola/
│       ├── cadastro_aluno.html
│       ├── cadastro_curso.html
│       ├── index.html
│       ├── lista_alunos.html
│       └── lista_cursos.html
├── tests.py                    # Arquivo para testes da aplicação
├── urls.py                     # Definições de URLs e roteamento
└── views.py                    # Lógica de negócio e views da aplicação
```

## 3. Tecnologias Utilizadas

*   **Django**: Framework web de alto nível para Python.
*   **Python**: Linguagem de programação principal.
*   **HTML/CSS**: Para a interface do usuário (através dos templates).
*   **SQLite** (provável, padrão do Django para desenvolvimento): Banco de dados.

## 4. Funcionalidades Principais

O Sistema Educacional oferece as seguintes funcionalidades:

*   **Cadastro de Alunos**: Permite adicionar novos alunos ao sistema.
*   **Listagem de Alunos**: Exibe uma lista de todos os alunos cadastrados.
*   **Cadastro de Cursos**: Permite adicionar novos cursos ao sistema.
*   **Listagem de Cursos**: Exibe uma lista de todos os cursos disponíveis.
*   **Painel Administrativo**: Gerenciamento de dados através da interface de administração do Django.

## 5. Modelos de Dados

### Aluno

*   `aluno.py`: Define o modelo para Alunos, incluindo campos como nome, matrícula, etc. (detalhes específicos dos campos dependeriam do conteúdo do arquivo `aluno.py`).

### Curso

*   `curso.py`: Define o modelo para Cursos, incluindo campos como nome do curso, descrição, etc. (detalhes específicos dos campos dependeriam do conteúdo do arquivo `curso.py`).

## 6. Configuração e Execução (Ambiente de Desenvolvimento)

Para configurar e executar o projeto em seu ambiente de desenvolvimento, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

*   Python 3.x
*   pip (gerenciador de pacotes do Python)

### Instalação

1.  Clone o repositório:
    ```bash
    git clone https://github.com/rafaelcrb/Sistema-Educacional.git
    cd Sistema-Educacional
    ```
2.  Crie e ative um ambiente virtual (recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # venv\Scripts\activate   # No Windows
    ```
3.  Instale as dependências do projeto (assumindo que há um `requirements.txt` ou que o Django será instalado manualmente):
    ```bash
    pip install Django
    # ou pip install -r requirements.txt (se existir)
    ```
4.  Execute as migrações do banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  Crie um superusuário para acessar o painel administrativo (opcional):
    ```bash
    python manage.py createsuperuser
    ```

### Execução

1.  Inicie o servidor de desenvolvimento Django:
    ```bash
    python manage.py runserver
    ```
2.  Acesse o aplicativo no seu navegador em `http://127.0.0.1:8000/` (ou a porta indicada).
3.  O painel administrativo estará disponível em `http://127.0.0.1:8000/admin/`.

## 7. Considerações de Desenvolvimento

*   O projeto utiliza o padrão MVC (Model-View-Controller, adaptado para MVT - Model-View-Template no Django) para organização do código.
*   A separação de modelos, views, URLs e templates facilita a manutenção e escalabilidade.
*   As migrações garantem a consistência do esquema do banco de dados.


