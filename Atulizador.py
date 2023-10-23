import os
import subprocess
from scripts import main_menu

# Diretório
repo_directory = ".\Documents\Mirage\codigos"

# URL 
repo_url = "https://github.com/AsterixNine/MirageGlass.git"

# Função para clonar ou atualizar o repositório
def update_repository():
    if os.path.exists(repo_directory):
        # Se o diretório do repositório já existe, faça um 'git pull' para atualizá-lo
        subprocess.call(["git", "pull"], cwd=repo_directory)
    else:
        # Caso contrário, faça um 'git clone' para clonar o repositório
        subprocess.call(["git", "clone", repo_url, repo_directory])

# Chame a função para atualizar o repositório
update_repository()
