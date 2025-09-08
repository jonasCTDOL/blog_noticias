# Importa a biblioteca do sistema
import sys, os

# Adiciona o diretório da aplicação ao 'path' do Python para que ele encontre seus arquivos
# INTERP... é uma variável especial do Phusion Passenger
INTERP = os.path.expanduser("~/venv/bin/python")
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

# Adiciona o diretório atual ao path para encontrar o app.py
sys.path.append(os.getcwd())

# Importa a variável 'app' do seu arquivo 'app.py'
from app import app as application