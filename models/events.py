from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from . import Base
from enum import Enum as EnumPython


class EventField(EnumPython):
    START_DATE = 1
    END_DATE = 2
    LOCATION = 3
    PARTICIPANTS = 4
    NOTE = 5
    CONTRACT_ID = 6
    SUPPORT_ID = 7


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

    def get_contract(self):
        return self.contract
