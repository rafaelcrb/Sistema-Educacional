# Sistema Educacional

Um sistema web simples para gerenciamento de alunos e cursos, desenvolvido com o framework Django.

## ✨ Funcionalidades

*   **Cadastro de Alunos**: Adicione novos alunos ao sistema.
*   **Listagem de Alunos**: Visualize todos os alunos cadastrados.
*   **Cadastro de Cursos**: Adicione novos cursos.
*   **Listagem de Cursos**: Visualize os cursos disponíveis.
*   **Painel Administrativo**: Gerencie dados através da interface de administração do Django.

## 🚀 Tecnologias Utilizadas

*   **Django**: Framework web Python.
*   **Python**: Linguagem de programação.
*   **HTML/CSS**: Para a interface do usuário.
*   **SQLite**: Banco de dados (padrão para desenvolvimento).

## ⚙️ Instalação e Execução

Para rodar este projeto em seu ambiente local, siga os passos abaixo:

### Pré-requisitos

*   Python 3.x
*   pip

### Passos

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
3.  Instale as dependências (assumindo que o Django será instalado):
    ```bash
    pip install Django
    ```
4.  Execute as migrações do banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  (Opcional) Crie um superusuário para o painel administrativo:
    ```bash
    python manage.py createsuperuser
    ```
6.  Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
    Acesse o aplicativo em `http://127.0.0.1:8000/` e o painel administrativo em `http://127.0.0.1:8000/admin/`.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


