# Skina

**Descrição:**
O Skina é um aplicativo desenvolvido com Django para gerenciar listas de compras. Ele possui um CRUD completo para manipular listas de produtos organizados em várias categorias, oferecendo uma experiência prática e eficiente para o usuário.

---

## Funcionalidades

- Criar, visualizar, editar e excluir listas de compras.
- Adicionar produtos a uma lista, com a possibilidade de classificá-los por categorias.
- Gerenciar categorias de produtos de maneira dinâmica.
- Interface amigável e intuitiva para facilitar o uso.

---

## Tecnologias utilizadas

- **Django:** Framework web principal.
- **SQLite (ou outro banco de dados de sua escolha):** Para armazenamento dos dados.
- **REST Framewor:** Para desenvolvimento da interface de API.

---

## Pré-requisitos

Antes de começar, certifique-se de que você tem o seguinte instalado em sua máquina:

- Python 3.8+
- Pip (Python package installer)
- Virtualenv

---

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/skina.git
   cd skina
   ```
2. Crie e ative um ambiente virtual (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate # Para sistemas Unix
   venv\Scripts\activate # Para Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```
5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
6. Acesse o aplicativo no navegador em:
   http://localhost:8000

---

## Estrutura de pastas
   ```
   skina/
├── manage.py
├── skina/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── lista_compras/  # Aplicação principal
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── static/
   ```