# ---------------------------------------------------------------------------
# ARQUIVO: app.py (VERSÃO COM PAINEL DE ADMINISTRAÇÃO)
# ---------------------------------------------------------------------------

# Importamos novas funções do Flask:
# - request: Para acessar os dados enviados por um formulário.
# - redirect: Para redirecionar o usuário para outra página após uma ação.
# - url_for: Para construir URLs dinamicamente para nossas rotas.
import click
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Nosso "banco de dados" temporário.
posts = [
    {
        'title': 'Bem-vindo ao Painel de Admin!',
        'content': 'Use o formulário acima para adicionar uma nova notícia ou exclua esta para começar.'
    }
]

# --- ROTAS PÚBLICAS (O QUE OS VISITANTES VEEM) ---

@app.route('/')
def index():
    """ Rota da página inicial que exibe todos os posts. """
    return render_template('index.html', posts=posts)


# --- ROTAS DE ADMINISTRAÇÃO (PARA GERENCIAR O CONTEÚDO) ---

@app.route('/admin')
def admin():
    """
    Exibe a página de administração com o formulário de adição
    e a lista de posts existentes para gerenciamento.
    """
    return render_template('admin.html', posts=posts)


@app.route('/add', methods=['POST'])
def add_post():
    """
    Esta rota não tem uma página, ela apenas processa os dados do formulário.
    Ela só aceita requisições do tipo POST.
    """
    # Pega o 'title' e o 'content' dos campos do formulário na página admin.html
    title = request.form['title']
    content = request.form['content']
    
    # Adiciona o novo post à nossa lista
    posts.append({'title': title, 'content': content})
    
    # Redireciona o usuário de volta para a página de admin para ver a lista atualizada.
    # url_for('admin') gera a URL '/admin' dinamicamente.
    return redirect(url_for('admin'))


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    """
    Rota dinâmica para deletar um post. O ID do post é passado na URL.
    Exemplo: /delete/0 vai deletar o primeiro post da lista.
    """
    # Verifica se o ID do post é válido para evitar erros
    if 0 <= post_id < len(posts):
        # O método .pop() remove um item da lista pelo seu índice
        posts.pop(post_id)
        
    # Redireciona o usuário de volta para a página de admin
    return redirect(url_for('admin'))


# --- COMANDO DE TERMINAL (Ainda útil para testes) ---

@app.cli.command("create-post")
@click.argument("title")
@click.argument("content")
def create_post_command(title, content):
    """ Cria um novo post no blog a partir da linha de comando. """
    posts.append({'title': title, 'content': content})
    print(f"✅ Post '{title}' criado com sucesso!")