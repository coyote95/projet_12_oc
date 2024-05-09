import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from unittest.mock import patch
from controllers.role_controllers import RoleController
from functools import wraps
from models import User




@pytest.fixture(scope="function")
def users():
    commercial=User("lucas", "lucas@test.com", "commercial", "password")
    gestion=User("julien", "julien@test.com", "gestion", "password")
    support=User("paul", "paul@test.com", "support", "password")
    return [commercial,gestion,support]

@pytest.fixture(scope="function")
def db_session():
    engine = create_engine("sqlite:///:memory:", echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    yield session  # Fournir la session aux tests

    session.commit()
    session.close()


def apply_patches(func):
    @wraps(func)
    def wrapper(db_session, *args, **kwargs):
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
            return func(db_session, *args, **kwargs)
    return wrapper
