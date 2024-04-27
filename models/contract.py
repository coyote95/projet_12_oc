from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime, Boolean, func
from sqlalchemy.orm import relationship
from . import Base


class Contract(Base):
    __tablename__ = 'contract'

    id = Column(Integer, primary_key=True)
    total_amount = Column(Float)
    remaining_amount = Column(Float)
    creation_date = Column(DateTime)
    signed_contract = Column(Boolean)
    # one to many(1 client pour plusieurs contract)
    client_id = Column(Integer, ForeignKey('client.id', ondelete='SET NULL'))  # one to many
    client = relationship("Client", back_populates='contracts')
    # one to one(1 evenement pour 1 contract)
    event = relationship("Event", back_populates="contract")

    # one to many(1 utilisateur pour plusieurs contracts)
    # user_id =  Column(Integer, ForeignKey('user.id', ondelete='SET NULL'))
    # user = relationship('User', back_populates="contracts")

    def __init__(self, total_amount, remaining_amount, client_id):
        self.total_amount = total_amount
        self.remaining_amount = remaining_amount
        self.client_id = client_id
        self.creation_date = func.now()
        self.event = None

    def __str__(self):
        return (f"<Contract(id='{id}', client='{self.client_id}', prix: {self.total_amount}, reste à payer: "
                f"{self.remaining_amount})>")

    def __repr__(self):
        return (f"<Contract(id='{id}', client='{self.client_id}', prix: {self.total_amount}, reste à payer: "
                f"{self.remaining_amount})>")

    def get_total_amount(self):
        return self.total_amount

    def get_remaining_amount(self):
        return self.remaining_amount

    def get_client(self):
        return self.client_id

    def get_event(self):
        return self.event
