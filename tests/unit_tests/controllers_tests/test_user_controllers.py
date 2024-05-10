from controllers.users_controllers import UserController
from ...conftest import patched_session, session_all_instances
from views.users_view import UserView
from models import User
from unittest.mock import MagicMock


def test_create_user(patched_session):
    # Créer une instance UserController
    user_controller = UserController()
    # Créer un mock pour UserView
    mock_user_view = MagicMock(spec=UserView)
    # Définir les entrées simulées pour la vue utilisateur
    mock_user_view.input_infos_user.return_value = ("John", "john@example.com", "commercial", "password")
    # Injecter la vue simulée dans le UserController
    user_controller.view = mock_user_view
    # Simuler l'ajout d'un nouvel utilisateur à la base de données
    new_user = user_controller.create_user()
    # Vérifier que la méthode input_infos_user() a été appelée
    mock_user_view.input_infos_user.assert_called_once()
    # Vérifier que les propriétés de l'utilisateur créé sont correctes
    find_user = User.filter_by_id(new_user.id)
    assert find_user.name == "John"


def test_delete_user_by_id(session_all_instances):
    user, client, contract, event, session = session_all_instances
    mock_user_view = MagicMock(spec=UserView)

    user_controller = UserController()
    user_controller.view = mock_user_view

    mock_user_view.input_id_user.return_value = 1

    user_exists = session.query(User).filter_by(id=1).first()
    assert user_exists == user

    user_controller.delete_user_by_id()

    mock_user_view.input_id_user.assert_called_once()
    mock_user_view.display_info_message.assert_called_once_with("Utilisateur supprimé avec succès.")

    user_still_exists = session.query(User).filter_by(id=1).first()
    assert user_still_exists is None


def test_delete_user_by_id_not_found(patched_session):
    mock_user_view = MagicMock(spec=UserView)

    user_controller = UserController()
    user_controller.view = mock_user_view

    mock_user_view.input_id_user.return_value = 1

    user_controller.delete_user_by_id()

    mock_user_view.input_id_user.assert_called_once()
    mock_user_view.display_warning_message.assert_called_once_with("Utilisateur non trouvé.")


def test_update_name_user(session_all_instances):
    user, client, contract, event, session = session_all_instances
    assert user.get_name() == "marc"
    mock_user_view = MagicMock(spec=UserView)

    user_controller = UserController()
    user_controller.view = mock_user_view

    mock_user_view.input_id_user.return_value = 1

    mock_user_view.ask_user_update_field.return_value = "nom"
    mock_user_view.input_name.return_value = "kevin"

    user_controller.update_user()
    mock_user_view.display_info_message.assert_called_once_with("Nom de l'utilisateur modifié avec succès.")
    assert user.get_name() == "kevin"


def test_update_departement_user(session_all_instances):
    user, client, contract, event, session = session_all_instances
    assert user.get_departement() == "commercial"
    mock_user_view = MagicMock(spec=UserView)

    user_controller = UserController()
    user_controller.view = mock_user_view

    mock_user_view.input_id_user.return_value = 1

    mock_user_view.ask_user_update_field.return_value = "departement"
    mock_user_view.input_departement.return_value = "gestion"

    user_controller.update_user()
    mock_user_view.display_info_message.assert_called_once_with("Département de l'utilisateur modifié avec succès.")
    assert user.get_departement() == "gestion"


def test_update_email_user(session_all_instances):
    user, client, contract, event, session = session_all_instances
    assert user.get_email() == "marc@test.com"
    mock_user_view = MagicMock(spec=UserView)

    user_controller = UserController()
    user_controller.view = mock_user_view

    mock_user_view.input_id_user.return_value = 1

    mock_user_view.ask_user_update_field.return_value = "email"
    mock_user_view.input_email.return_value = "marco@test.fr"

    user_controller.update_user()
    mock_user_view.display_info_message.assert_called_once_with("Email de l'utilisateur modifié avec succès.")
    assert user.get_email() == "marco@test.fr"


def test_update_password_user(session_all_instances):
    user, client, contract, event, session = session_all_instances
    assert user.check_password("password")
    mock_user_view = MagicMock(spec=UserView)

    user_controller = UserController()
    user_controller.view = mock_user_view

    mock_user_view.input_id_user.return_value = 1

    mock_user_view.ask_user_update_field.return_value = "password"
    mock_user_view.input_password.return_value = "marcolito"

    user_controller.update_user()
    mock_user_view.display_info_message.assert_called_once_with("Mot de passe de l'utilisateur modifié avec succès.")
    assert user.check_password("marcolito")
