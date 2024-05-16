from controllers import ClientController
from views.clients_view import ClientView
from models import Client
from unittest.mock import MagicMock


def test_create_and_delete_client(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    client_controller = ClientController()
    mock_client_view = MagicMock(spec=ClientView)
    mock_client_view.input_info_client.return_value = ("tarault", "manon", "manon@test.com", "0123654789",
                                                       "darty")
    client_controller.view = mock_client_view
    new_client = client_controller.create_client(user.id)
    mock_client_view.input_info_client.assert_called_once()
    find_client = Client.filter_by_id(new_client.id)
    assert find_client.surname == "manon"
    mock_client_view.display_info_message.assert_called_once_with("Création client réussite !")

    mock_client_view.reset_mock()
    mock_client_view.input_id_client.return_value = find_client.id
    assert client.get_commercial_id() == user.id
    client_exists = session.query(Client).filter_by(id=find_client.id).first()
    assert client_exists == find_client
    client_controller.delete_client_by_id(user.id)
    mock_client_view.input_id_client.assert_called_once()
    mock_client_view.display_info_message.assert_called_once_with("Client supprimé avec succès.")
    client_still_exists = session.query(Client).filter_by(id=find_client.id).first()
    assert client_still_exists is None
