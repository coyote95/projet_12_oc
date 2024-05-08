#
# from models import Base, User
# import pytest
# from settings.database import engine, Session
#
#
#
# # Vos tests unitaires commencent ici
#
#
#
# @pytest.fixture
# def test_session():
#     # Créer une nouvelle session pour les tests
#     test_session = Session()
#     yield test_session
#     # Fermer la session après le test
#     test_session.close()
#
#
# class TestUserCreation:
#     def test_create_user(self, test_session):
#         # Votre logique de test ici
#         Base.metadata.create_all(engine)
#
#         user = User("jean", "lucazzkkkeeezzeeeeees@teeest2.com", "commercial", "password")
#         test_session.add(user)
#         test_session.commit()
#
#         # Assurez-vous que les modifications sont bien enregistrées
#         assert test_session.query(User).filter_by(name="jean").first() is not None
#
#     def test_create2_user(self, test_session):
#         # Votre logique de test ici
#         Base.metadata.create_all(engine)
#
#         user = User("jean", "lucazzkkkeeezzeeeeees@teeest2.com", "commercial", "password")
#         test_session.add(user)
#         test_session.commit()
#
#         # Assurez-vous que les modifications sont bien enregistrées
#         assert test_session.query(User).filter_by(name="jean").first() is not None
#
#
#     # Cette méthode sera exécutée après chaque test pour nettoyer la base de données
#     def teardown_method(self):
#         test_session = Session()
#         print("okeeeeeeeeeeeeeeeeeeeeeeee")
#         test_session.query(User).delete()
#         test_session.commit()
