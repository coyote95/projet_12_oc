import os
from dotenv import load_dotenv

current_dir = os.path.dirname(__file__)  # Chemin absolu du répertoire contenant settings.py
parent_dir = os.path.dirname(current_dir)  # Chemin absolu du répertoire parent

dotenv_path = os.path.join(parent_dir, '.env')
load_dotenv(dotenv_path)

secret_key = os.getenv('SECRET_KEY')
database = os.getenv('DATABASE')



