from controllers.contract_controllers import ContractController
from controllers.clients_controllers import ClientController
from views.contract_view import ContractView
from views.clients_view import ClientView
from models import Contract
from unittest.mock import MagicMock
from models import Client,User


def test_create_user(all_instances):

    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)

    # new_gestionnaire = User("valentin", "valentin@test.com", "gestion", "password")
    # session.add(new_gestionnaire)
    session.commit()

    mock_contract_view = MagicMock(spec=ContractView)
    contract_controller = ContractController()
    contract_controller.view=mock_contract_view

    mock_contract_view.input_id_client.return_value=1
    mock_contract_view.input_total_price.return_value = 200
    mock_contract_view.input_remaining_price.return_value = 100
    mock_contract_view.input_signed_contract.return_value = True

    new_contract = contract_controller.create_contract(user.role,user.id)

    print(new_contract)
    mock_contract_view.input_total_price.assert_called_once()

    find_contract = Contract.filter_by_id(new_contract.id)
    assert find_contract.total_price == 200
