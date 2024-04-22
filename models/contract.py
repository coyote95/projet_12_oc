from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from . import Base


class Contract(Base):
    __tablename__ = 'contract'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))  # relation dans la table
    client = relationship("Client")  # relation modele python
    sales_contact = Column(String(255)) # users?
    total_amount = Column(Float)
    remaining_amount = Column(Float)
    creation_date = Column(DateTime)
    signed_contract = Column(Boolean)
    events = relationship("Event",backref="contracts")


