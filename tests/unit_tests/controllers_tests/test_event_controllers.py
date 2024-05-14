from controllers.contract_controllers import ContractController
from controllers.clients_controllers import ClientController
from controllers.event_controllers import EventController
from views.contract_view import ContractView
from views.event_view import EventView
from views.clients_view import ClientView
from models import Contract, Event
from unittest.mock import MagicMock
from datetime import datetime



def test_create_event(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    session.commit()

    mock_event_view = MagicMock(spec=EventView)
    event_controller = EventController()
    event_controller.view = mock_event_view

    mock_event_view.input_id_contract.return_value = 1
    mock_event_view.input_start_date.return_value = datetime(2024, 12, 29, 12, 30)
    mock_event_view.input_end_date.return_value = datetime(2025, 12, 29, 12, 30)
    mock_event_view.input_infos_event.return_value = ("paris","20",'RAS')
    mock_event_view.input_id_support.return_value = 1
    new_event = event_controller.create_event(user.id)

    mock_event_view.input_infos_event.assert_called_once()

    find_event = Event.filter_by_id(new_event.id)
    assert find_event.location == "paris"
