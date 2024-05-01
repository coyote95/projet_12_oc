from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime, Boolean, func
from sqlalchemy.orm import relationship
from . import Base
from enum import Enum as EnumPython


class ContractField(EnumPython):
    TOTAL_PRICE = 1
    REMAINING_PRICE = 2
    SIGNED = 3
    CLIENT_ID = 4
    EVENT = 5


class Contract(Base):
    __tablename__ = 'contract'

    id = Column(Integer, primary_key=True)
    total_price = Column(Float)
    remaining_price = Column(Float)
    creation_date = Column(DateTime)
    signed_contract = Column(Boolean)
    # one to many(1 client pour plusieurs contract) contract=child
    client_id = Column(Integer, ForeignKey('client.id', ondelete='SET NULL'))  # one to many
    client = relationship("Client", back_populates='contracts')
    # one to one(1 evenement pour 1 contract)
    event = relationship("Event", back_populates="contract", uselist=False)

    # one to many(1 utilisateur pour plusieurs contracts)
    # user_id =  Column(Integer, ForeignKey('user.id', ondelete='SET NULL'))
    # user = relationship('User', back_populates="contracts")

    def __init__(self, total_price, remaining_price, signed_contract, client_id):
        self.total_price = total_price
        self.remaining_price = remaining_price
        self.signed_contract = signed_contract
        self.client_id = client_id
        self.creation_date = func.now()

    def __str__(self):
        return (f"<Contrat:(id='{id}', client='{self.client_id}', prix= {self.total_price}, reste à payer= "
                f"{self.remaining_price})>")

    def __repr__(self):
        return (f"<Contrat:(id='{id}', client='{self.client_id}', prix= {self.total_price}, reste à payer= "
                f"{self.remaining_price})>")

    def get_id(self):
        return self.id

    def get_total_price(self):
        return self.total_price

    def get_remaining_price(self):
        return self.remaining_price

    def get_client_id(self):
        return self.client_id

    def get_event(self):
        return self.event

    def get_client(self):
        return self.client

    def get_signed_contract(self):
        return self.signed_contract

    def set_id(self, contract_id):
        self.id = contract_id

    def set_total_price(self, total_price):
        self.total_price = total_price

    def set_remaining_price(self, remaining_price):
        self.remaining_price = remaining_price

    def set_signed_contract(self, signed_contract):
        self.signed_contract = signed_contract

    def set_client_id(self, client_id):
        self.client_id = client_id

    def set_client(self, client):
        self.client = client

    def set_event(self, event):
        self.event = event
