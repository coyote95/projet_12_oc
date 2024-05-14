from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from . import Base
from settings.database import session


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    email = Column(String(255), unique=True)
    phone = Column(String(10))
    company = Column(String(255))
    creation_date = Column(DateTime)
    last_update_date = Column(DateTime)
    # one to many (1 utilisateur peut avoir plusieur client) client=child
    commercial_id = Column(Integer, ForeignKey('user.id', ondelete='SET NULL'))
    commercial = relationship('User', back_populates='clients')
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
