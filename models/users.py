import bcrypt
from sqlalchemy import Column, String, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from models.role import Role
from . import Base
from settings.database import session


class User(Base):
    """
       Represents a user entity in the database.

       Attributes:
           id (int): The unique identifier for the user.
           name (str): The name of the user.
           email (str): The email address of the user (unique).
           department (Enum): The department of the user, which can be one of 'commercial', 'support', or 'gestion'.
           password (str): The hashed password of the user.
           clients (relationship): Relationship with the Client model representing clients associated with the user.
           role (relationship): Relationship with the Role model representing the role of the user.
           events (relationship): Relationship with the Event model representing events associated with the user.

       Methods:
           __init__(name, email, department, password): Initializes a new User object with the provided attributes.
           __str__(): Returns a string representation of the User object.
           __repr__(): Returns a string representation of the User object.
           get_id(): Returns the user's ID.
           get_name(): Returns the user's name.
           get_email(): Returns the user's email address.
           get_department(): Returns the user's department.
           get_password(): Returns the user's hashed password.
           set_id(user_id): Sets the user's ID.
           set_name(name): Sets the user's name.
           set_email(email): Sets the user's email address.
           set_department(department): Sets the user's department.
           set_password(password): Sets and hashes the user's password.
           check_password(password): Checks if the provided password matches the user's hashed password.
           set_role_from_department(): Sets the user's role based on their department.
           get_clients_name(): Returns a list of names of clients associated with the user.
           filter_by_id(user_id): Returns the user with the specified ID.
           filter_all_users(): Returns all users in the database.
       """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    departement = Column(Enum('commercial', 'support', 'gestion'))
    password = Column(String(255))
    # one to many(1 user can have multiple clients)
    clients = relationship('Client', back_populates="commercial", passive_deletes='all')
    # one to many (1 role can have multiple users)
    role_id = Column(Integer, ForeignKey('role.id', ondelete='SET NULL'))
    role = relationship('Role', back_populates="users")
    # one to many(1 support can have multiple events)
    events = relationship('Event', back_populates="support", passive_deletes='all')

    def __init__(self, name, email, departement, password):
        self.name = name
        self.email = email
        self.departement = departement
        self.password = self.set_password(password)
        self.set_role_from_departement()

    def __str__(self):
        return f"<User(nom='{self.name}', password='{self.password}')>"

    def __repr__(self):
        return f"<User(nom='{self.name}', password='{self.password}')>"

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_departement(self):
        return self.departement

    def get_password(self):
        return self.password

    def set_id(self, user_id):
        self.id = user_id

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_departement(self, departement):
        self.departement = departement

    def set_password(self, password):
        if password is not None:
            self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return self.password

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def set_role_from_departement(self):
        if self.departement == 'commercial':
            self.role = session.query(Role).filter_by(role='commercial').first()
        elif self.departement == 'gestion':
            self.role = session.query(Role).filter_by(role='gestion').first()
        elif self.departement == 'support':
            self.role = session.query(Role).filter_by(role='support').first()
        else:
            raise ValueError("Invalid department value")

    def get_clients_name(self):
        return [client.name for client in self.clients] if self.clients else []

    @staticmethod
    def filter_by_id(user_id):
        return session.query(User).filter_by(id=user_id).first()

    @staticmethod
    def filter_all_users():
        return session.query(User).all()
