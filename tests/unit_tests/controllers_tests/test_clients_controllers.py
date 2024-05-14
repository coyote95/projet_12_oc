from controllers.clients_controllers import ClientController
from views.clients_view import ClientView
from models import Client,User
from unittest.mock import MagicMock


def test_create_user(init_session):
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


def test_delete_client_by_id(all_instances):
    user, client, contract, event, session = all_instances
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


def test_delete_client_by_id_not_found(all_instances):
    user, client, contract, event, session = all_instances
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


def test_delete_client_by_id_not_your_team(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(3)
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = 1
    client_controller.delete_client_by_id(2)
    mock_client_view.input_id_client.assert_called_once()
    mock_client_view.display_warning_message.assert_called_once_with("Ce client ne fait pas partie de votre équipe")


def test_update_name_client(all_instances):
    user, client, contract, event, session = all_instances
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

def test_update_surname_client(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    assert client.get_surname() == "alice"
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = 1
    mock_client_view.ask_client_update_field.return_value = "prenom"
    mock_client_view.input_surname.return_value = "laura"
    client_controller.update_client(user.id)
    mock_client_view.display_info_message.assert_called_once_with("Prénom du client modifié avec succès.")
    assert client.get_surname() == "laura"

def test_update_email_client(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    assert client.get_email() == "alice@example.com"
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = 1
    mock_client_view.ask_client_update_field.return_value = "email"
    mock_client_view.input_email.return_value = "laura@test.com"
    client_controller.update_client(user.id)
    mock_client_view.display_info_message.assert_called_once_with("Email du client modifié avec succès.")
    assert client.get_email() == "laura@test.com"

def test_update_telephone_client(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    assert client.get_phone() == "0123456780"
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = 1
    mock_client_view.ask_client_update_field.return_value = "telephone"
    mock_client_view.input_phone.return_value = "0123654789"
    client_controller.update_client(user.id)
    mock_client_view.display_info_message.assert_called_once_with("Téléphone du client modifié avec succès.")
    assert client.get_phone() == "0123654789"

def test_update_entreprise_client(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    assert client.get_company() == "DARTY"
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = 1
    mock_client_view.ask_client_update_field.return_value = "entreprise"
    mock_client_view.input_company.return_value = "KFC"
    client_controller.update_client(user.id)
    mock_client_view.display_info_message.assert_called_once_with("Entreprise du client modifié avec succès.")
    assert client.get_company() == "KFC"

def test_update_commercial_client(all_instances):
    user, client, contract, event, session = all_instances
    new_commercial = User("valentin", "valentin@test.com", "commercial", "password")
    session.add(new_commercial)
    session.commit()
    client.set_commercial_id(user.id)
    assert client.get_commercial_id() == 1
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = 1
    mock_client_view.ask_client_update_field.return_value = "commercial"
    mock_client_view.input_id_commercial.return_value = "2"
    client_controller.update_client(user.id)
    mock_client_view.display_info_message.assert_called_once_with("Commercial du client modifié avec succès.")
    assert client.get_commercial_id() == 2


def test_update_commercial_client_invalid(all_instances):
    user, client, contract, event, session = all_instances
    new_commercial = User("valentin", "valentin@test.com", "gestion", "password")
    session.add(new_commercial)
    session.commit()
    client.set_commercial_id(user.id)
    assert client.get_commercial_id() == 1
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = 1
    mock_client_view.ask_client_update_field.return_value = "commercial"
    mock_client_view.input_id_commercial.return_value = "2"
    client_controller.update_client(user.id)
    mock_client_view.display_warning_message.assert_called_once_with("L'ID spécifié n'appartient pas à un commercial.")
    assert client.get_commercial_id() == 1

def test_update_client_not_found(all_instances):
    user, client, contract, event, session = all_instances
    mock_client_view = MagicMock(spec=ClientView)
    client_controller = ClientController()
    client_controller.view = mock_client_view
    mock_client_view.input_id_client.return_value = 2
    mock_client_view.ask_client_update_field.return_value = "nom"
    mock_client_view.input_name.return_value = "dupont"
    client_controller.update_client(user.id)
    mock_client_view.display_warning_message("Aucun client trouvé avec cet ID")

