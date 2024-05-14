from controllers import UserController
from views import UserView
from models import User
from unittest.mock import MagicMock


def test_create_user(init_session):
    user_controller = UserController()
    mock_user_view = MagicMock(spec=UserView)
    mock_user_view.input_infos_user.return_value = ("John", "j1hn@example.com", "commercial", "password")
    user_controller.view = mock_user_view
    new_user = user_controller.create_user()
    mock_user_view.input_infos_user.assert_called_once()
    find_user = User.filter_by_id(new_user.id)
    assert find_user.name == "John"


def test_delete_user_by_id(all_instances):
    user, client, contract, event, session = all_instances
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


def test_delete_user_by_id_not_found(init_session):
    mock_user_view = MagicMock(spec=UserView)
    user_controller = UserController()
    user_controller.view = mock_user_view
    mock_user_view.input_id_user.return_value = 1
    user_controller.delete_user_by_id()
    mock_user_view.input_id_user.assert_called_once()
    mock_user_view.display_warning_message.assert_called_once_with("Utilisateur non trouvé.")


def test_update_name_user(all_instances):
    user, client, contract, event, session = all_instances
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


def test_update_departement_user(all_instances):
    user, client, contract, event, session = all_instances
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


def test_update_email_user(all_instances):
    user, client, contract, event, session = all_instances
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


def test_update_password_user(all_instances):
    user, client, contract, event, session = all_instances
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
