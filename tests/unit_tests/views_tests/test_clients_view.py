from unittest.mock import patch, MagicMock
from views.clients_view import ClientView


def test_input_name_return_upper(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Lucas')
    assert ClientView.input_name() == 'LUCAS'


def test_input_surname_return_upper(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Dupont')
    assert ClientView.input_surname() == 'DUPONT'


def test_input_company_return_lower(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Darty')
    assert ClientView.input_company() == 'darty'


def test_input_phone_invalid_less_numbers(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['123456', '1234567890']):
        ClientView.input_phone()

    captured = capsys.readouterr()
    assert captured.out == "ERROR: Votre numéro ne comporte pas 10 chiffres\n"


def test_input_phone_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1234567890']):
        ClientView.input_phone()

    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_input_id_client_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1234567890']):
        ClientView.input_id_client()

    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_input_id_commercial_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1234567890']):
        ClientView.input_id_commercial()

    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_ask_client_update_field_1(monkeypatch, capsys):
    with patch('builtins.input', return_value="1"):
        assert ClientView.ask_client_update_field() == "nom"


def test_ask_client_update_field_2(monkeypatch, capsys):
    with patch('builtins.input', return_value="2"):
        assert ClientView.ask_client_update_field() == "prenom"


def test_ask_client_update_field_3(monkeypatch, capsys):
    with patch('builtins.input', return_value="3"):
        assert ClientView.ask_client_update_field() == "email"


def test_ask_client_update_field_4(monkeypatch, capsys):
    with patch('builtins.input', return_value="4"):
        assert ClientView.ask_client_update_field() == "telephone"


def test_ask_client_update_field_5(monkeypatch, capsys):
    with patch('builtins.input', return_value="5"):
        assert ClientView.ask_client_update_field() == "entreprise"


def test_ask_client_update_field_6(monkeypatch, capsys):
    with patch('builtins.input', return_value="6"):
        assert ClientView.ask_client_update_field() == "commercial"


def test_ask_client_update_field_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1']):
        ClientView.ask_client_update_field()

    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_ask_client_update_field_7(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['7', '1']):
        ClientView.ask_client_update_field()

    captured = capsys.readouterr()
    assert captured.out == "WARNING: Vous n'avez pas saisi un numéro valide\n"
