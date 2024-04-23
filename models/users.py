import bcrypt
from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.orm import relationship
from models.role import user_role_association, Role
from . import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    departement = Column(Enum('commercial', 'support', 'gestion'))
    password = Column(String(255))
    clients = relationship('Client', backref="users")
    roles = relationship('Role', secondary=user_role_association, backref="users")

    def __init__(self, name, email, departement, password):
        self.name = name
        self.email = email
        self.departement = departement
        self.roles = self.set_role_from_departement()
        self.password = self.set_password(password)

    def __str__(self):
        return f"<User(nom='{self.name}', password='{self.password}')>"

    def __repr__(self):
        return f"<User(nom='{self.name}', password='{self.password}')>"

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

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

    def set_role_from_departement(self):
        if self.departement == 'commercial':
            return [Role(role='commercial')]
        elif self.departement == 'gestion':
            return [Role(role='gestion')]
        elif self.departement == 'support':
            return [Role(role='support')]
        else:
            raise ValueError("Invalid departement value")