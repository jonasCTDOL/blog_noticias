import os
import pymysql
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Adiciona o suporte ao PyMySQL
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# --- CONFIGURAÇÃO DO BANCO DE DADOS ---
# Usaremos variáveis de ambiente ou placeholders por enquanto
DB_USER = 'SEU_USUARIO_DB'
DB_PASS = 'SUA_SENHA_DB'
DB_HOST = 'localhost'
DB_NAME = 'SEU_NOME_DB'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODELO DA TABELA DE POSTS ---
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# --- COMANDO PARA CRIAR A TABELA NO SERVIDOR ---
@app.cli.command("init-db")
def init_db_command():
    """Cria as tabelas do banco de dados."""
    db.create_all()
    print("Banco de dados inicializado e tabela 'post' criada.")

# --- ROTAS MODIFICADAS ---
@app.route('/')
def index():
    # Busca todos os posts do banco de dados
    all_posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', posts=all_posts)
    
@app.route('/admin')
def admin():
    all_posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('admin.html', posts=all_posts)

@app.route('/add', methods=['POST'])
def add_post():
    # Adiciona um novo post no banco de dados
    title = request.form['title']
    content = request.form['content']
    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    # Deleta um post do banco de dados pelo seu ID
    post_to_delete = Post.query.get_or_404(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('admin'))