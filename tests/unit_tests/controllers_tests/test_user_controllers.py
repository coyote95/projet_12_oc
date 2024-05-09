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
    user_controller.model = user

    mock_user_view.input_id_user.return_value = user.id

    user_controller.model.filter_by_id.return_value = user
    user_still_exists = session.query(User).filter_by(id=user.id).first()
    print("88888888888888888")
    print(user_still_exists)
    # Appeler la méthode delete_user_by_id()
    user_controller.delete_user_by_id()

    # Appeler la méthode delete_user_by_id()
    # user_controller.delete_user_by_id()

    # Vérifier que la méthode input_id_user() a été appelée
    mock_user_view.input_id_user.assert_called_once()

    # Vérifier que la méthode filter_by_id() a été appelée avec le bon ID d'utilisateur
    # user_controller.model.filter_by_id.assert_called_once_with(1)
    print("99999999999999999999999999999999999999999999999999")
    user_still_exists = session.query(User).filter_by(id=user.id).first()

    user_still_exists = session.query(User).filter_by(id=user.id).first()
    print(user_still_exists)
    # assert user_still_exists is None
    # Vérifier que la méthode display_info_message() a été appelée avec le bon message
    mock_user_view.display_info_message.assert_called_once_with("Utilisateur supprimé avec succès.")
