from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.clients import Client
from models.contract import Contract
from . import Base
from settings.database import session


class Event(Base):
    """
       Represents an event entity in the database.

       Attributes:
           id (int): The unique identifier for the event.
           start_date (DateTime): The start date and time of the event.
           end_date (DateTime): The end date and time of the event.
           location (str): The location of the event.
           participants (int): The number of participants in the event.
           notes (str): Any additional notes related to the event.
           contract_id (int): The foreign key referencing the contract associated with the event.
           contract (relationship): Relationship with the Contract model representing the contract associated with the event.
           support_id (int): The foreign key referencing the user providing support for the event.
           support (relationship): Relationship with the User model representing the support user for the event.

       Methods:
           __init__(start_date, end_date, location, participants, notes): Initializes a new Event object with provided attributes.
           __str__(): Returns a string representation of the Event object.
           get_id(): Returns the ID of the event.
           get_start_date(): Returns the start date and time of the event.
           get_end_date(): Returns the end date and time of the event.
           get_location(): Returns the location of the event.
           get_participants(): Returns the number of participants in the event.
           get_notes(): Returns any additional notes related to the event.
           get_support(): Returns the support user for the event.
           get_support_id(): Returns the ID of the support user for the event.
           get_contract(): Returns the contract associated with the event.
           get_contract_id(): Returns the ID of the contract associated with the event.
           set_id(event_id): Sets the ID of the event.
           set_start_date(start_date): Sets the start date and time of the event.
           set_end_date(end_date): Sets the end date and time of the event.
           set_location(location): Sets the location of the event.
           set_participants(participants): Sets the number of participants in the event.
           set_notes(notes): Sets any additional notes related to the event.
           set_support(support): Sets the support user for the event.
           set_support_id(support_id): Sets the ID of the support user for the event.
           set_contract(contract): Sets the contract associated with the event.
           set_contract_id(contract_id): Sets the ID of the contract associated with the event.
           verify_date_end(): Verifies if the end date is earlier than the start date for the event.
           filter_by_contract_id(contract_id): Returns the event with the specified contract ID.
           filter_by_id(event_id): Returns the event with the specified ID.
           find_commercial_id(event_id): Finds the commercial ID associated with the event.
           filter_all_events(): Returns all events.
           filter_by_support(support_id): Returns all events supported by the specified user.
           filter_by_none_support(): Returns all events with no assigned support user.
       """
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    location = Column(String(255))
    participants = Column(Integer)
    notes = Column(String(255))
    # one to one(1 contrat can have 1 evenement)
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
