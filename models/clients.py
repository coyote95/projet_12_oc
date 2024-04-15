from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    nom_complet = Column(String)
    email = Column(String, unique=True)
    telephone = Column(String)
    entreprise = Column(String)

    def __repr__(self):
        return f"<Client(nom_complet='{self.nom_complet}', email='{self.email}', téléphone='{self.telephone}', entreprise='{self.entreprise}')>"
