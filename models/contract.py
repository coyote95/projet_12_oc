from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime, Boolean, func
from sqlalchemy.orm import relationship
from . import Base
from settings.database import session


class Contract(Base):
    """
    Represents a contract entity in the database.

    Attributes:
        id (int): The unique identifier for the contract.
        total_price (float): The total price of the contract.
        remaining_price (float): The remaining amount to be paid for the contract.
        creation_date (DateTime): The date and time when the contract was created.
        signed (bool): A boolean indicating whether the contract is signed or not.
        client_id (int): The foreign key referencing the client associated with the contract.
        client (relationship): Relationship with the Client model representing the client associated with the contract.
        event (relationship): Relationship with the Event model representing the event associated with the contract.

    Methods:
        __init__(total_price, remaining_price, signed, client_id=None): Initializes a new Contract object with provided attributes.
        __str__(): Returns a string representation of the Contract object.
        __repr__(): Returns a string representation of the Contract object.
        get_id(): Returns the ID of the contract.
        get_total_price(): Returns the total price of the contract.
        get_remaining_price(): Returns the remaining price of the contract.
        get_client_id(): Returns the ID of the client associated with the contract.
        get_event(): Returns the event associated with the contract.
        get_client(): Returns the client associated with the contract.
        get_signed(): Returns whether the contract is signed or not.
        set_id(contract_id): Sets the ID of the contract.
        set_total_price(total_price): Sets the total price of the contract.
        set_remaining_price(remaining_price): Sets the remaining price of the contract.
        set_signed(signed): Sets whether the contract is signed or not.
        set_client_id(client_id): Sets the client ID associated with the contract.
        set_client(client): Sets the client associated with the contract.
        set_event(event): Sets the event associated with the contract.
        filter_by_id(contract_id): Returns the contract with the specified ID.
        filter_all_contracts(): Returns all contracts.
        filter_unsigned(): Returns all unsigned contracts.
        filter_unpayed(): Returns all contracts with remaining price not equal to 0.
    """

    __tablename__ = "contract"

    id = Column(Integer, primary_key=True)
    total_price = Column(Float)
    remaining_price = Column(Float)
    creation_date = Column(DateTime)
    signed = Column(Boolean)
    # one to many(1 client can have multipe contract) contract=child
    client_id = Column(Integer, ForeignKey("client.id", ondelete="SET NULL"))
    client = relationship("Client", back_populates="contracts")
    # one to one(1 event can have  1 contract)
    event = relationship("Event", back_populates="contract", uselist=False)

    def __init__(self, total_price, remaining_price, signed, client_id=None):
        self.total_price = total_price
        self.remaining_price = remaining_price
        self.signed = signed
        self.client_id = client_id
        self.creation_date = func.now()

    def __str__(self):
        return (
            f"<Contrat:(id='{id}', client='{self.client_id}', prix= {self.total_price}, reste à payer= "
            f"{self.remaining_price})>"
        )

    def __repr__(self):
        return (
            f"<Contrat:(id='{id}', client='{self.client_id}', prix= {self.total_price}, reste à payer= "
            f"{self.remaining_price})>"
        )

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

    def get_signed(self):
        return self.signed

    def set_id(self, contract_id):
        self.id = contract_id

    def set_total_price(self, total_price):
        self.total_price = total_price

    def set_remaining_price(self, remaining_price):
        self.remaining_price = remaining_price

    def set_signed(self, signed):
        self.signed = signed

    def set_client_id(self, client_id):
        self.client_id = client_id

    def set_client(self, client):
        self.client = client

    def set_event(self, event):
        self.event = event

    @staticmethod
    def filter_by_id(contract_id):
        return session.query(Contract).filter_by(id=contract_id).first()

    @staticmethod
    def filter_all_contracts():
        return session.query(Contract).all()

    @staticmethod
    def filter_unsigned():
        return session.query(Contract).filter_by(signed=False).all()

    @staticmethod
    def filter_unpayed():
        return session.query(Contract).filter(Contract.remaining_price != 0).all()
