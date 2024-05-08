import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine("sqlite:///:memory:", echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    yield session  # Fournir la session aux tests

    session.commit()
    session.close()
