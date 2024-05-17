from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from . import Base
from settings.database import session


class Client(Base):
    """
    Represents a client entity in the database.

    Attributes:
        id (int): The unique identifier for the client.
        name (str): The name of the client.
        surname (str): The surname of the client.
        email (str): The email address of the client (unique).
        phone (str): The phone number of the client.
        company (str): The company of the client.
        creation_date (DateTime): The date and time when the client was created.
        last_update_date (DateTime): The date and time when the client was last updated.
        commercial_id (int): The foreign key referencing the user who is the commercial associated with the client.
        commercial (relationship): Relationship with the User model representing the commercial associated with the client.
        contracts (relationship): Relationship with the Contract model representing the contracts associated with the client.

    Methods:
        __init__(name, surname, email, phone, company): Initializes a new Client object with provided attributes.
        __repr__(): Returns a string representation of the Client object.
        get_id(): Returns the ID of the client.
        get_name(): Returns the name of the client.
        get_surname(): Returns the surname of the client.
        get_email(): Returns the email of the client.
        get_phone(): Returns the phone number of the client.
        get_company(): Returns the company of the client.
        get_creation_date(): Returns the creation date of the client.
        get_last_update_date(): Returns the last update date of the client.
        get_commercial_id(): Returns the ID of the commercial associated with the client.
        get_user_name(): Returns the name of the commercial associated with the client.
        set_last_update_date(): Updates the last update date of the client to the current datetime.
        set_id(client_id): Sets the ID of the client.
        set_name(name): Sets the name of the client.
        set_surname(surname): Sets the surname of the client.
        set_email(email): Sets the email of the client.
        set_phone(phone): Sets the phone number of the client.
        set_company(company): Sets the company of the client.
        set_commercial_id(user_id): Sets the commercial ID associated with the client.
        filter_by_id(client_id): Returns the client with the specified ID.
        filter_all_clients(): Returns all clients.
        filter_by_commercial_id(commercial_id): Returns all clients associated with the specified commercial ID.
    """

    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    email = Column(String(255), unique=True)
    phone = Column(String(10))
    company = Column(String(255))
    creation_date = Column(DateTime)
    last_update_date = Column(DateTime)
    # one to many (1 user can have multiple clients) client=child
    commercial_id = Column(Integer, ForeignKey("user.id", ondelete="SET NULL"))
    commercial = relationship("User", back_populates="clients")
    # one to many (1 client can have multiple contract ou event) client=parents
    contracts = relationship("Contract", back_populates="client", passive_deletes="all")

    def __init__(self, name, surname, email, phone, company):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.company = company
        self.creation_date = func.now()
        self.last_update_date = func.now()

    def __repr__(self):
        return (
            f"<Client(nom_complet='{self.name}', email='{self.email}', téléphone='{self.phone}', entreprise="
            f"'{self.company}')>"
        )

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

    def get_commercial_id(self):
        return self.commercial_id

    def get_user_name(self):
        return self.commercial.name if self.commercial else None

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

    def set_commercial_id(self, user_id):
        self.commercial_id = user_id

    @staticmethod
    def filter_by_id(client_id):
        return session.query(Client).filter_by(id=client_id).first()

    @staticmethod
    def filter_all_clients():
        return session.query(Client).all()

    @staticmethod
    def filter_by_commercial_id(commercial_id):
        return session.query(Client).filter_by(commercial_id=commercial_id).all()
