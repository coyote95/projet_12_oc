from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Importez les modèles individuels ici
from .users import User
from .clients import Client
from .contract import Contract
from .events import Event
from .role import Role

# Ajoutez d'autres imports si nécessaire
