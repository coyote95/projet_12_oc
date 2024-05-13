from unittest.mock import patch
from views.event_view import EventView
from datetime import datetime


def test_input_id_contract_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1']):
        EventView.input_id_contract()
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_input_participants_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1']):
        EventView.input_participants()
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_input_id_event_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1']):
        EventView.input_id_event()
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_input_id_support_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1']):
        EventView.input_id_support()
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_input_start_date(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2024-12-29 12:30')
    assert EventView.input_start_date() == datetime.strptime('2024-12-29 12:30:00', "%Y-%m-%d %H:%M:%S")


def test_input_start_date_invalid(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['2024-12', '2024-12-29 12:30']):
        EventView.input_start_date()
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Format de date incorrect. Utilisez le format YYYY-MM-DD HH:MM.\n"


def test_input_location_upper(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Paris')
    assert EventView.input_location() == 'PARIS'


def test_ask_event_update_field_contract_oui(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'oui')
    assert EventView.ask_event_update_field_support_id() == True


def test_ask_event_update_field_contract_non(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'non')
    assert EventView.ask_event_update_field_support_id() == False


def test_input_signed_contract_invalid(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', 'oui']):
        EventView.ask_event_update_field_support_id()
    captured = capsys.readouterr()
    assert "Vous n'avez pas saisi 'oui' ou 'non'" in captured.out


def test_ask_event_update_field_1(monkeypatch, capsys):
    with patch('builtins.input', return_value="1"):
        assert EventView.ask_event_update_field() == "date_debut"


def test_ask_event_update_field_2(monkeypatch, capsys):
    with patch('builtins.input', return_value="2"):
        assert EventView.ask_event_update_field() == "date_fin"

def test_ask_event_update_field_3(monkeypatch, capsys):
    with patch('builtins.input', return_value="3"):
        assert EventView.ask_event_update_field() == "localisation"


def test_ask_event_update_field_4(monkeypatch, capsys):
    with patch('builtins.input', return_value="4"):
        assert EventView.ask_event_update_field() == "participant"

def test_ask_event_update_field_5(monkeypatch, capsys):
    with patch('builtins.input', return_value="5"):
        assert EventView.ask_event_update_field() == "note"


def test_ask_event_update_field_6(monkeypatch, capsys):
    with patch('builtins.input', return_value="6"):
        assert EventView.ask_event_update_field() == "contrat"

def test_ask_event_update_field_7(monkeypatch, capsys):
    with patch('builtins.input', return_value="7"):
        assert EventView.ask_event_update_field() == "support"

def test_ask_client_update_field_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1']):
        EventView.ask_event_update_field()

    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_ask_client_update_field_8(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['8', '1']):
        EventView.ask_event_update_field()

    captured = capsys.readouterr()
    assert captured.out == "WARNING: Vous n'avez pas saisi un numéro valide\n"

