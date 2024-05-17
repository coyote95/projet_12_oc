from controllers import EventController
from views import EventView
from models import Event, User
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
    mock_event_view.input_infos_event.return_value = ("paris", "20", "RAS")
    mock_event_view.input_id_support.return_value = 1
    new_event = event_controller.create_event(user.id)
    mock_event_view.input_infos_event.assert_called_once()
    find_event = Event.filter_by_id(new_event.id)
    assert find_event.location == "paris"


def test_create_event_with_contract_false(all_instances):
    user, client, contract, event, session = all_instances
    contract.signed = False
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    session.commit()
    mock_event_view = MagicMock(spec=EventView)
    event_controller = EventController()
    event_controller.view = mock_event_view
    mock_event_view.input_id_contract.return_value = 1
    mock_event_view.input_start_date.return_value = datetime(2024, 12, 29, 12, 30)
    mock_event_view.input_end_date.return_value = datetime(2025, 12, 29, 12, 30)
    mock_event_view.input_infos_event.return_value = ("paris", "20", "RAS")
    mock_event_view.input_id_support.return_value = 1
    event_controller.create_event(user.id)
    mock_event_view.display_warning_message.assert_called_once_with(
        "Ce client n'a pas encore signé le contrat"
    )
    find_event = Event.filter_by_id(2)
    assert find_event is None


def test_delete_event_by_id(all_instances):
    user, client, contract, event, session = all_instances
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    event.set_contract_id(contract.id)
    session.commit()
    mock_event_view = MagicMock(spec=EventView)
    event_controller = EventController()
    event_controller.view = mock_event_view
    mock_event_view.input_id_event.return_value = 1
    event_exists = session.query(Event).filter_by(id=1).first()
    assert event_exists == event
    event_controller.delete_event_by_id(user.id)
    mock_event_view.input_id_event.assert_called_once()
    mock_event_view.display_info_message.assert_called_once_with(
        "Evénement supprimé avec succès."
    )
    event_still_exists = session.query(Event).filter_by(id=1).first()
    assert event_still_exists is None


def test_update_location_event(all_instances):
    user, client, contract, event, session = all_instances
    user_support = User("louis", "louis@test.com", "support", "password")
    session.add(user_support)
    session.commit()
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    event.set_contract_id(contract.id)
    event.set_support_id(user_support.id)
    session.commit()
    assert event.get_location() == "madrid"
    mock_event_view = MagicMock(spec=EventView)
    event_controller = EventController()
    event_controller.view = mock_event_view
    mock_event_view.input_id_event.return_value = event.id
    mock_event_view.ask_event_update_field.return_value = "localisation"
    mock_event_view.input_location.return_value = "nice"
    event_controller.update_event(user.role, user_support.id)
    mock_event_view.display_info_message.assert_called_once_with(
        "Localisation modifié avec succès."
    )
    assert event.get_location() == "nice"


def test_update_start_date_event(all_instances):
    user, client, contract, event, session = all_instances
    user_support = User("louis", "louis@test.com", "support", "password")
    session.add(user_support)
    session.commit()
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    event.set_contract_id(contract.id)
    event.set_support_id(user_support.id)
    session.commit()
    assert event.get_start_date() == datetime(2024, 5, 15, 12, 30)
    mock_event_view = MagicMock(spec=EventView)
    event_controller = EventController()
    event_controller.view = mock_event_view
    mock_event_view.input_id_event.return_value = event.id
    mock_event_view.ask_event_update_field.return_value = "date_debut"
    mock_event_view.input_start_date.return_value = datetime(2025, 5, 15, 12, 30, 00)
    event_controller.update_event(user.role, user_support.id)
    mock_event_view.display_info_message.assert_called_once_with(
        "Date de début modifié avec succès."
    )
    assert event.get_start_date() == datetime(2025, 5, 15, 12, 30, 00)


def test_update_end_date_event(all_instances):
    user, client, contract, event, session = all_instances
    user_support = User("louis", "louis@test.com", "support", "password")
    session.add(user_support)
    session.commit()
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    event.set_contract_id(contract.id)
    event.set_support_id(user_support.id)
    session.commit()
    assert event.get_end_date() == datetime(2024, 5, 16, 12, 30)
    mock_event_view = MagicMock(spec=EventView)
    event_controller = EventController()
    event_controller.view = mock_event_view
    mock_event_view.input_id_event.return_value = event.id
    mock_event_view.ask_event_update_field.return_value = "date_fin"
    mock_event_view.input_end_date.return_value = datetime(2025, 5, 15, 12, 30, 00)
    event_controller.update_event(user.role, user_support.id)
    mock_event_view.display_info_message.assert_called_once_with(
        "Date de fin modifié avec succès."
    )
    assert event.get_end_date() == datetime(2025, 5, 15, 12, 30, 00)


def test_update_participant_event(all_instances):
    user, client, contract, event, session = all_instances
    user_support = User("louis", "louis@test.com", "support", "password")
    session.add(user_support)
    session.commit()
    client.set_commercial_id(user.id)
    contract.set_client_id(client.id)
    event.set_contract_id(contract.id)
    event.set_support_id(user_support.id)
    session.commit()
    assert event.get_participants() == 50
    mock_event_view = MagicMock(spec=EventView)
    event_controller = EventController()
    event_controller.view = mock_event_view
    mock_event_view.input_id_event.return_value = event.id
    mock_event_view.ask_event_update_field.return_value = "participant"
    mock_event_view.input_participants.return_value = 20
    event_controller.update_event(user.role, user_support.id)
    mock_event_view.display_info_message.assert_called_once_with(
        "Nombre de participants modifié avec succès."
    )
    assert event.get_participants() == 20
