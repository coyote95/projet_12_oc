from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))  # relation dans la table
    client = relationship("Client")  # relation modele python
    sales_contact = Column(String) # users?
    total_amount = Column(Float)
    remaining_amount = Column(Float)
    creation_date = Column(DateTime)
    signed_contract = Column(Boolean)


