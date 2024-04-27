from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from . import Base


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, ForeignKey('contract.id', ondelete='SET NULL'))
    contract = relationship("Contract", back_populates='event')
    client_id = Column(Integer, ForeignKey('client.id', ondelete='SET NULL'))
    client = relationship("Client", back_populates='events')
    client_contact = Column(String(255))  # voir relation clien
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    support_contact = Column(String(255))  # voir relation user
    location = Column(String(255))
    participants = Column(Integer)
    notes = Column(String(255))
