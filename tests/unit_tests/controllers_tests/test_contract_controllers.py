from controllers.contract_controllers import ContractController
from controllers.clients_controllers import ClientController
from views.contract_view import ContractView
from views.clients_view import ClientView
from models import Contract
from unittest.mock import MagicMock
from models import Client, User


def test_create_contract(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)

    # new_gestionnaire = User("valentin", "valentin@test.com", "gestion", "password")
    # session.add(new_gestionnaire)
    session.commit()

    mock_contract_view = MagicMock(spec=ContractView)
    contract_controller = ContractController()
    contract_controller.view = mock_contract_view

    mock_contract_view.input_id_client.return_value = 1
    mock_contract_view.input_total_price.return_value = 200
    mock_contract_view.input_remaining_price.return_value = 100
    mock_contract_view.input_signed_contract.return_value = True

    new_contract = contract_controller.create_contract(user.role, user.id)

    print(new_contract)
    mock_contract_view.input_total_price.assert_called_once()

    find_contract = Contract.filter_by_id(new_contract.id)
    assert find_contract.total_price == 200


def test_delete_contract_by_id(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    mock_contract_view = MagicMock(spec=ContractView)
    contract_controller = ContractController()
    contract_controller.view = mock_contract_view
    mock_contract_view.input_id_contract.return_value = 1
    assert client.get_commercial_id() == user.id
    contract_exists = session.query(Contract).filter_by(id=1).first()
    assert contract_exists == contract
    contract_controller.delete_contract_by_id(user.role, user.id)
    mock_contract_view.input_id_contract.assert_called_once()
    mock_contract_view.display_info_message.assert_called_once_with("Contrat supprimé avec succès.")
    user_still_exists = session.query(Contract).filter_by(id=1).first()
    assert user_still_exists is None


def test_delete_contract_by_id_not_found(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    mock_contract_view = MagicMock(spec=ContractView)
    contract_controller = ContractController()
    contract_controller.view = mock_contract_view
    mock_contract_view.input_id_contract.return_value = 2
    assert client.get_commercial_id() == user.id
    contract_exists = session.query(Contract).filter_by(id=2).first()
    assert contract_exists is None
    contract_controller.delete_contract_by_id(user.role, user.id)
    mock_contract_view.input_id_contract.assert_called_once()
    mock_contract_view.display_warning_message.assert_called_once_with("contrat non trouvé.")


def test_delete_contract_by_id_not_your_team(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(3)
    contract.set_client_id(client.id)
    mock_contract_view = MagicMock(spec=ContractView)
    contract_controller = ContractController()
    contract_controller.view = mock_contract_view
    mock_contract_view.input_id_contract.return_value = 1
    contract_controller.delete_contract_by_id(user.role, user.id)
    mock_contract_view.input_id_contract.assert_called_once()
    mock_contract_view.display_warning_message.assert_called_once_with(
        "Ce contrat de client ne fait pas partie de votre équipe")


def test_update_total_price_contract(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    session.commit()
    assert contract.get_total_price() == 1000.0
    mock_contract_view = MagicMock(spec=ContractView)
    contract_controller = ContractController()
    contract_controller.view = mock_contract_view
    mock_contract_view.input_id_contract.return_value = 1
    mock_contract_view.ask_contract_update_field.return_value = "prix_total"
    mock_contract_view.input_total_price.return_value = 500.0
    contract_controller.update_contract(user.role, user.id)
    mock_contract_view.display_info_message.assert_called_once_with("Prix total modifié avec succès.")
    assert contract.get_total_price() == 500.0


def test_update_remaining_price_contract(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    session.commit()
    assert contract.get_remaining_price() == 500.0
    mock_contract_view = MagicMock(spec=ContractView)
    contract_controller = ContractController()
    contract_controller.view = mock_contract_view
    mock_contract_view.input_id_contract.return_value = 1
    mock_contract_view.ask_contract_update_field.return_value = "prix_restant"
    mock_contract_view.input_remaining_price.return_value = 100.0
    contract_controller.update_contract(user.role, user.id)
    mock_contract_view.display_info_message.assert_called_once_with("Prix restant modifié avec succès.")
    assert contract.get_remaining_price() == 100.0


def test_update_signature_contract(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    session.commit()
    assert contract.get_signed() is True
    mock_contract_view = MagicMock(spec=ContractView)
    contract_controller = ContractController()
    contract_controller.view = mock_contract_view
    mock_contract_view.input_id_contract.return_value = 1
    mock_contract_view.ask_contract_update_field.return_value = "signature"
    mock_contract_view.input_signed_contract.return_value = False
    contract_controller.update_contract(user.role, user.id)
    mock_contract_view.display_info_message.assert_called_once_with("Statut signature modifié avec succès.")
    assert contract.get_signed() is False


def test_update_client_contract(all_instances):
    user, client, contract, event, session = all_instances
    new_client = Client("pol", "adrien", "adrien@test.com", "0123456780", "BUT")
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    session.add(new_client)
    session.commit()
    assert contract.client_id == client.id
    mock_contract_view = MagicMock(spec=ContractView)
    contract_controller = ContractController()
    contract_controller.view = mock_contract_view
    mock_contract_view.input_id_contract.return_value = 1
    mock_contract_view.ask_contract_update_field.return_value = "client"
    mock_contract_view.input_id_client.return_value = 2
    contract_controller.update_contract(user.role, user.id)
    mock_contract_view.display_info_message.assert_called_once_with("Client du contrat modifié avec succès.")
    assert contract.get_client_id() == 2


def test_update_contract_not_found(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    session.commit()
    mock_contract_view = MagicMock(spec=ContractView)
    contract_controller = ContractController()
    contract_controller.view = mock_contract_view
    mock_contract_view.input_id_contract.return_value = 2
    mock_contract_view.ask_contract_update_field.return_value = "signature"
    mock_contract_view.input_signed_contract.return_value = True
    contract_controller.update_contract(user.role, user.id)
    mock_contract_view.display_warning_message("Aucun contrat trouvé avec cet ID")
