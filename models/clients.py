from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base


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
    user_id = Column(Integer, ForeignKey('user.id', ondelete='SET NULL'))
    user = relationship('User', back_populates='clients')
    contracts = relationship("Contract", backref="clients")
    events = relationship("Event", backref="clients")

    def __init__(self, name, surname, email, phone, company):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.company = company
        self.creation_date = func.now()
        self.last_update_date= func.now()

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

    def get_user_name(self):
        return self.user.name if self.user else None


