from controllers.clients_controllers import ClientController
from ...conftest import patched_session, session_all_instances
from views.clients_view import ClientView
from models import Client
from unittest.mock import MagicMock


def test_create_user(patched_session):
    # Créer une instance UserController
    client_controller = ClientController()
    # Créer un mock pour UserView
    mock_client_view = MagicMock(spec=ClientView)
    # Définir les entrées simulées pour la vue utilisateur
    mock_client_view.input_info_client.return_value = ("tarault", "manon", "manon@test.com", "0123654789",
                                                       "darty")
    # Injecter la vue simulée dans le UserController
    client_controller.view = mock_client_view
    # Simuler l'ajout d'un nouvel utilisateur à la base de données
    new_client = client_controller.create_client(1)
    # Vérifier que la méthode input_infos_user() a été appelée
    mock_client_view.input_info_client.assert_called_once()
    # Vérifier que les propriétés de l'utilisateur créé sont correctes
    find_client = Client.filter_by_id(new_client.id)
    assert find_client.surname == "manon"


def test_delete_client_by_id(session_all_instances):
    user, client, contract, event, session = session_all_instances
    client.set_commercial_id(user.id)
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = client.id
    assert client.get_commercial_id() == user.id
    client_exists = session.query(Client).filter_by(id=1).first()
    assert client_exists == client
    client_controller.delete_client_by_id(client.id)
    mock_client_view.input_id_client.assert_called_once()
    mock_client_view.display_info_message.assert_called_once_with("Client supprimé avec succès.")
    user_still_exists = session.query(Client).filter_by(id=1).first()
    assert user_still_exists is None


def test_delete_client_by_id_not_found(session_all_instances):
    user, client, contract, event, session = session_all_instances
    client.set_commercial_id(user.id)
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = 2
    assert client.get_commercial_id() == user.id
    client_exists = session.query(Client).filter_by(id=2).first()
    assert client_exists is None
    client_controller.delete_client_by_id(2)
    mock_client_view.input_id_client.assert_called_once()
    mock_client_view.display_warning_message.assert_called_once_with("Client non trouvé.")


def test_delete_client_by_id_not_your_team(session_all_instances):
    user, client, contract, event, session = session_all_instances
    client.set_commercial_id(3)
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = 1
    client_controller.delete_client_by_id(2)
    mock_client_view.input_id_client.assert_called_once()
    mock_client_view.display_warning_message.assert_called_once_with("Ce client ne fait pas partie de votre équipe")


def test_update_name_client(session_all_instances):
    user, client, contract, event, session = session_all_instances
    client.set_commercial_id(user.id)
    assert client.get_name() == "martin"
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = 1
    mock_client_view.ask_client_update_field.return_value = "nom"
    mock_client_view.input_name.return_value = "dupont"
    client_controller.update_client(user.id)
    mock_client_view.display_info_message.assert_called_once_with("Nom du client modifié avec succès.")
    assert client.get_name() == "dupont"

def test_update_client_not_found(session_all_instances):
    user, client, contract, event, session = session_all_instances
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = 2
    mock_client_view.ask_client_update_field.return_value = "nom"
    mock_client_view.input_name.return_value = "dupont"
    client_controller.update_client(user.id)
    mock_client_view.display_warning_message("Aucun client trouvé avec cet ID")


# def test_display_error_message():
#     # Créer un objet MagicMock pour simuler ClientView
#     mock_client_view = MagicMock(spec=ClientView)
#
#     # Appeler la méthode display_error_message avec le message d'erreur spécifié
#     mock_client_view.display_error_message("Votre numéro ne comporte pas 10 chiffres")
#
#     # Vérifier si display_error_message a été appelée avec le bon message d'erreur
#     mock_client_view.display_error_message.assert_called_with("Votre numéro ne comporte pas 10 chiffres")
#


    # with patch('builtins.input', side_effect=['abc', '1234567890']):
    #     ClientView.input_phone()
    #
    # captured = capsys.readouterr()
    # assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"

# from unittest.mock import patch

# def test_input_phone_invalid_should_return_none(monkeypatch, capsys):
#     # Simuler une entrée utilisateur invalide
#     monkeypatch.setattr('builtins.input', lambda _: 'abc')
#
#     # Utiliser patch pour éviter que le test ne boucle indéfiniment
#     with patch('builtins.input', side_effect=['123456', 'abc', '1234567890']):
#         assert ClientView.input_phone() == 1234567890
#
#     # Capturer la sortie d'erreur standard pour vérifier le message d'erreur
#     captured = capsys.readouterr()
#
#     # Vérifier si l'un ou l'autre des messages d'erreur est présent dans la sortie capturée
#     assert "ERROR: Votre numéro ne comporte pas 10 chiffres" in captured.out
#     assert "ERROR: Vous n'avez pas saisi un numéro" in captured.out
