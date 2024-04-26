import bcrypt
from sqlalchemy import Column, String, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from models.role import Role
from . import Base
from config import session

from enum import Enum as EnumPython


class UserField(EnumPython):
    NOM = 1
    DEPARTEMENT = 2
    CLIENTS = 3


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    departement = Column(Enum('commercial', 'support', 'gestion'))
    password = Column(String(255))
    clients = relationship('Client', back_populates="user", passive_deletes='all')
    role_id = Column(Integer, ForeignKey('role.id', ondelete='SET NULL'))
    role = relationship('Role', back_populates="users")

    def __init__(self, name, email, departement, password):
        self.name = name
        self.email = email
        self.departement = departement
        self.password = self.set_password(password)
        self.role = self.set_role_from_departement(departement)

    def __str__(self):
        return f"<User(nom='{self.name}', password='{self.password}')>"

    def __repr__(self):
        return f"<User(nom='{self.name}', password='{self.password}')>"

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_departement(self):
        return self.departement

    def get_password(self):
        return self.password

    def set_password(self, password):
        # Hasher et saler le mot de passe
        if password is not None:
            self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return self.password

    def check_password(self, password):
        # Vérifier si le mot de passe fourni correspond au mot de passe stocké
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def set_role_from_departement(self, departement):
        if departement == 'commercial':
            return session.query(Role).filter_by(role='commercial').first()
        elif departement == 'gestion':
            return session.query(Role).filter_by(role='gestion').first()
        elif departement == 'support':
            return session.query(Role).filter_by(role='support').first()
        else:
            raise ValueError("Invalid department value")
