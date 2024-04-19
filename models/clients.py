from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    phone = Column(String(255))
    company = Column(String(255))


    def __init__(self, name, email, phone, company):
        self.name = name
        self.email = email
        self.phone = phone
        self.company = company

    def __repr__(self):
        return (f"<Client(nom_complet='{self.name}', email='{self.email}', téléphone='{self.phone}', entreprise="
                f"'{self.company}')>")
