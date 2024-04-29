from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as EnumPython
from . import Base


class ClientField(EnumPython):
    NOM = 1
    SURNAME = 2
    EMAIL = 3
    PHONE = 4
    COMPANY = 5


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    email = Column(String(255), unique=True)
    phone = Column(Integer)
    company = Column(String(255))
    creation_date = Column(DateTime)
    last_update_date = Column(DateTime)
    # one to many (1 utilisateur peut avoir plusieur client) client=child
    user_id = Column(Integer, ForeignKey('user.id', ondelete='SET NULL'))
    user = relationship('User', back_populates='clients')
    # one to many (1client peut avoir plusieur contract ou event) client = parents
    contracts = relationship("Contract", back_populates="client", passive_deletes='all')

    # events = relationship("Event", back_populates="client",passive_deletes='all')

    def __init__(self, name, surname, email, phone, company):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.company = company
        self.creation_date = func.now()
        self.last_update_date = func.now()

    def __repr__(self):
        return (f"<Client(nom_complet='{self.name}', email='{self.email}', téléphone='{self.phone}', entreprise="
                f"'{self.company}')>")

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_company(self):
        return self.company

    def get_creation_date(self):
        return self.creation_date

    def get_last_update_date(self):
        return self.last_update_date

    def get_user_id(self):
        return self.user_id

    def get_user_name(self):
        return self.user.name if self.user else None

    def set_last_update_date(self):
        self.last_update_date = func.now()

    def set_id(self, client_id):
        self.id = client_id

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def set_company(self, company):
        self.company = company

    def set_user_id(self, user_id):
        self.user_id = user_id
