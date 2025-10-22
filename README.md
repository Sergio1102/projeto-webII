# Sistema de Gestão de Eventos

Projeto final desenvolvido para a disciplina de Web II do curso de LCC. Trata-se de um sistema para criação, gerenciamento e inscrição em eventos.

## Funcionalidades Implementadas

* **Autenticação de Usuários:** Sistema completo de registro, login e logout.
* **Painel Administrativo Personalizado:** Área restrita para administradores gerenciarem todo o conteúdo do site, sem usar a interface `/admin` padrão do Django.
* **CRUD Completo:**
    * Gerenciamento de Eventos (com upload de banner)
    * Gerenciamento de Locais
    * Gerenciamento de Palestrantes (com upload de foto)
    * Gerenciamento de Categorias
* **Sistema de Inscrição:** Usuários autenticados podem se inscrever nos eventos.
* **Interatividade com HTMX:** A inscrição é feita de forma assíncrona, sem recarregar a página.
* **Design Responsivo:** Interface adaptável para desktops e dispositivos móveis usando CSS personalizado.

## Tecnologias Utilizadas

* **Backend:** Python 3, Django
* **Frontend:** HTML5, CSS3, HTMX
* **Banco de Dados:** SQLite3 (padrão do Django)
* **Dependências:** Pillow (para manipulação de imagens)

## Como Executar o Projeto Localmente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Sergio1102/projeto-webII.git](https://github.com/Sergio1102/projeto-webII.git)
    cd projeto-webII
    ```
2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # venv\Scripts\activate    # No Windows
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```
5.  **Crie um superusuário para acessar o painel administrativo:**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Execute o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
7.  Acesse `http://127.0.0.1:8000` no seu navegador.