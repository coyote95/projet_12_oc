import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from unittest.mock import patch
from controllers.role_controllers import RoleController
from models import User, Client, Contract, Event
from datetime import datetime


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine("sqlite:///:memory:", echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    yield session  # Fournir la session aux tests

    session.commit()
    session.close()


@pytest.fixture(scope="function")
def patched_session(db_session):
    with patch("models.users.session", db_session), \
            patch("models.clients.session", db_session), \
            patch("models.contract.session", db_session), \
            patch("models.events.session", db_session), \
            patch("models.users.session", db_session), \
            patch("controllers.role_controllers.session", db_session), \
            patch("controllers.clients_controllers.session", db_session), \
            patch("controllers.contract_controllers.session", db_session), \
            patch("controllers.event_controllers.session", db_session), \
            patch("controllers.users_controllers.session", db_session):
        role_controller = RoleController()
        role_controller.init_role_database()
        yield db_session


@pytest.fixture(scope="function")
def session_all_instances(patched_session):
    user = User("Marc", "john.doe@example.com", "commercial", "password")
    client = Client("Alice", "Smith", "alice@example.com", "1234567890", "XYZ Company")
    contract = Contract(total_price=1000.0, remaining_price=500.0, signed=True)
    event = Event(
        start_date=datetime(2024, 5, 15),
        end_date=datetime(2024, 5, 16),
        location="Conference Room",
        participants=50,
        notes="Example event",
    )
    client.commercial_id = user.id
    contract.client_id = client.id
    event.contract_id = contract.id
    patched_session.add(user)
    patched_session.commit()
    yield user, client, contract, event, patched_session
