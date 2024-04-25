from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
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
    last_update = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id',ondelete='SET NULL'))
    user = relationship('User', back_populates='clients')
    contracts = relationship("Contract", backref="clients")
    events = relationship("Event", backref="clients")

    def __init__(self, name, email, phone, company):
        self.name = name
        self.email = email
        self.phone = phone
        self.company = company

    def __repr__(self):
        return (f"<Client(nom_complet='{self.name}', email='{self.email}', téléphone='{self.phone}', entreprise="
                f"'{self.company}')>")
