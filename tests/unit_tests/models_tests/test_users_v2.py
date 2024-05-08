from models import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from settings.database import session,engine
import pytest

def test_create_user(monkeypatch):
    # Créez une nouvelle instance de moteur pour une base de données de test
    engine = create_engine("sqlite:///:memory:", echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    #
    # # Utilisez monkeypatch pour remplacer la session globale dans le module settings.database
    # monkeypatch.setattr("settings.database.session", new_session)
    # monkeypatch.setattr("settings.database.engine", test_engine)
    # Créez les tables dans la base de données de test
    Base.metadata.create_all(engine)

    # Créez un utilisateur et ajoutez-le à la base de données de test
    user = User("Lucas", "lu9cas@test.com", "commercial", "password")
    session.add(user)
    session.commit()

    # Vérifiez si l'utilisateur a été ajouté avec succès
    assert session.query(User).filter_by(name="Lucas").first() is not None

    # Fermez la session après le test
    session.close()
