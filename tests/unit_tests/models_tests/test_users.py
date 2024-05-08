from models import Base, User
from unittest.mock import patch
from ...fixture import db_session
from controllers.role_controllers import  RoleController



def test_filter_by_id(db_session):
    with patch("models.users.session", db_session):  # Remplace la session globale par db_session
        user = User("lucas", "lucas@test.com", "commercial", "password")
        db_session.add(user)
        db_session.commit()

        # Maintenant, user.filter_by_id utilisera la session de test
        find_user = user.filter_by_id(user.id)
        assert find_user.name == "lucas"

def test_role_from_departement(db_session):
    with patch("models.users.session", db_session):  # Remplace la session globale par db_session
        with patch("controllers.role_controllers.session", db_session):  # Remplace la session globale par
            # db_session
            role_controller = RoleController()
            role_controller.init_role_database()
            user = User("lucas", "luccas@test.com", "commercial", "password")
            db_session.add(user)
            db_session.commit()
            assert user.role_id == 1
