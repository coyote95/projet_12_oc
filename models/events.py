from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.clients import Client
from models.contract import Contract
from . import Base
from settings.database import session


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    location = Column(String(255))
    participants = Column(Integer)
    notes = Column(String(255))
    # one to one(1 contrat pour 1 evenement)
    contract_id = Column(Integer, ForeignKey('contract.id', ondelete='SET NULL'))
    contract = relationship("Contract", back_populates='event', uselist=False)
    # one to many(1support pour plusieurs event)
    support_id = Column(Integer, ForeignKey('user.id', ondelete='SET NULL'))  # voir relation user
    support = relationship('User', back_populates='events')

    def __init__(self, start_date, end_date, location, participants, notes):
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.participants = participants
        self.notes = notes

    def __str__(self):
        return (f"<Evennement: (id='{id}', date de début='{self.start_date}', date de fin: {self.end_date}, "
                f"localisation= {self.location}, participants={self.participants}, note={self.notes})>")

    def get_id(self):
        return self.id

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_location(self):
        return self.location

    def get_participants(self):
        return self.participants

    def get_notes(self):
        return self.notes

    def get_support(self):
        return self.support

    def get_support_id(self):
        return self.support_id

    def get_contract(self):
        return self.contract

    def get_contract_id(self):
        return self.contract_id

    def set_id(self, event_id):
        self.id = event_id

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_location(self, location):
        self.location = location

    def set_participants(self, participants):
        self.participants = participants

    def set_notes(self, notes):
        self.notes = notes

    def set_support(self, support):
        self.support = support

    def set_support_id(self, support_id):
        self.support_id = support_id

    def set_contract(self, contract):
        self.contract = contract

    def set_contract_id(self, contract_id):
        self.contract_id = contract_id

    def verify_date_end(self):
        return self.end_date < self.start_date

    @staticmethod
    def filter_by_contract_id(contract_id):
        return session.query(Event).filter_by(contract_id=contract_id).first()

    @staticmethod
    def filter_by_id(event_id):
        return session.query(Event).filter_by(id=event_id).first()

    @staticmethod
    def find_commercial_id(event_id):
        specific_user_id = (
            session.query(Client.commercial_id)
            .join(Contract, Contract.client_id == Client.id)
            .join(Event, Event.contract_id == Contract.id)
            .filter(Event.id == event_id)
            .first()
        )
        return specific_user_id[0]

    @staticmethod
    def filter_all_events():
        return session.query(Event).all()

    @staticmethod
    def filter_by_support(support_id):
        return session.query(Event).filter_by(support_id=support_id).all()

    @staticmethod
    def filter_by_none_support():
        return session.query(Event).filter(Event.support_id.is_(None)).all()
