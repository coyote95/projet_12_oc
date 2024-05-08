# fixtures.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

@pytest.fixture(scope="function")
def db_session():
    # Créez une nouvelle instance de moteur pour une base de données de test
    engine = create_engine("sqlite:///:memory:", echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Créez les tables dans la base de données de test
    Base.metadata.create_all(engine)

    yield session  # Fournir la session aux tests

    # Nettoyez la base de données après chaque test
    meta = Base.metadata
    for table in reversed(meta.sorted_tables):
        session.execute(table.delete())
    session.commit()
    session.close()

# test_users.py
def test_create_user(db_session):
    user = User("Lucas", "lu9cas@test.com", "commercial", "password")
    db_session.add(user)
    db_session.commit()

    # Vérifiez si l'utilisateur a été ajouté avec succès
    assert db_session.query(User).filter_by(name="Lucas").first() is not None

    # Utilisez db_session au lieu de session

    # Tout le reste du test reste inchangé

def test_create_user2(db_session):
    user = User("Lucas", "lu9cas@test.com", "commercial", "password")
    db_session.add(user)
    db_session.commit()

    # Vérifiez si l'utilisateur a été ajouté avec succès
    assert db_session.query(User).filter_by(name="Lucas").first() is not None

def test_create_user3(db_session):
    user = User("Lucas", "lu9cas@test.com", "commercial", "password")
    db_session.add(user)
    db_session.commit()

    # Vérifiez si l'utilisateur a été ajouté avec succès
    assert db_session.query(User).filter_by(name="Lucas").first() is not None
