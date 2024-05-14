from models import Base
from controllers.role_controllers import RoleController
from models import User, Client, Contract, Event
from datetime import datetime
from settings.database import engine
import pytest
from settings.database import session


@pytest.fixture
def init_session():
    Base.metadata.create_all(engine)
    role_controller = RoleController()
    role_controller.init_role_database()

    yield session  # Fournir la session aux tests

    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture
def all_instances(init_session):
    user = User("marc", "marc@test.com", "commercial", "password")
    client = Client("martin", "alice", "alice@example.com", "0123456780", "DARTY")
    contract = Contract(total_price=1000.0, remaining_price=500.0, signed=True)
    event = Event(
        start_date=datetime(2024, 5, 15,12,30),
        end_date=datetime(2024, 5, 16,12,30),
        location="madrid",
        participants=50,
        notes="RAS",
    )

    contract.client_id = client.id
    event.contract_id = contract.id
    init_session.add(user)
    init_session.add(client)
    init_session.add(contract)
    init_session.add(event)
    init_session.commit()
    yield user, client, contract, event, init_session
