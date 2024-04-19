from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# # Importez les modèles individuels ici
from .users import User
from .clients import Client
# # Ajoutez d'autres imports si nécessaire