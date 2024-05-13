from unittest.mock import patch
from views.contract_view import ContractView


def test_input_total_price_invalid_no_float(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1']):
        ContractView.input_total_price()
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_input_remaining_price_invalid_no_float(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1']):
        ContractView.input_remaining_price()
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_input_signed_contract_oui(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'oui')
    assert ContractView.input_signed_contract() == True


def test_input_signed_contract_non(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'non')
    assert ContractView.input_signed_contract() == False


def test_input_signed_contract_invalid(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', 'oui']):
        ContractView.input_signed_contract()
    captured = capsys.readouterr()
    assert "Vous n'avez pas saisi 'oui' ou 'non'" in captured.out


def test_input_id_contract_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1']):
        ContractView.input_id_contract()
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_ask_contract_update_field_1(monkeypatch, capsys):
    with patch('builtins.input', return_value="1"):
        assert ContractView.ask_contract_update_field() == "prix_total"


def test_ask_contract_update_field_2(monkeypatch, capsys):
    with patch('builtins.input', return_value="2"):
        assert ContractView.ask_contract_update_field() == "prix_restant"


def test_ask_contract_update_field_3(monkeypatch, capsys):
    with patch('builtins.input', return_value="3"):
        assert ContractView.ask_contract_update_field() == "signature"


def test_ask_contract_update_field_4(monkeypatch, capsys):
    with patch('builtins.input', return_value="4"):
        assert ContractView.ask_contract_update_field() == "client"


def test_ask_contract_update_field_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1']):
        ContractView.ask_contract_update_field()
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_ask_client_update_field_invalid(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['7', '1']):
        ContractView.ask_contract_update_field()
    captured = capsys.readouterr()
    assert captured.out == "WARNING: Vous n'avez pas saisi un numéro valide\n"


def test_menu_filter_1(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert ContractView.menu_filter() == 1
    captured = capsys.readouterr()
    assert captured.out == "Voici la liste des contrats non signés\n"


def test_menu_filter_2(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert ContractView.menu_filter() == 2
    captured = capsys.readouterr()
    assert captured.out == "Voici la liste des contrats non payés\n"


