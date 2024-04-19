from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Event(Base):
    __tablename__ = 'events'

    event_id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, ForeignKey('contracts.id'))
    contract = relationship("Contract")
    client_name = Column(Integer, ForeignKey('clients.id'))
    client = relationship("Client")
    client_contact = Column(String(255))  # voir relation clien
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    support_contact = Column(String(255))  # voir relation user
    location = Column(String(255))
    participants = Column(Integer)
    notes = Column(String(255))
