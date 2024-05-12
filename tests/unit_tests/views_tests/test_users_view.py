from unittest.mock import patch, MagicMock
from views.users_view import UserView


def test_input_name_return_upper(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Lucas')
    assert UserView.input_name() == 'LUCAS'


def test_input_email_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Lucas@test.com')
    assert UserView.input_email() == 'Lucas@test.com'


def test_input_email_invalid(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['Lucas_test.com', 'Lucas@test.com']):
        UserView.input_email()

    captured = capsys.readouterr()
    assert captured.out == "ERROR: Adresse email invalide. Veuillez réessayer.\n"


def test_input_departement_return_lower(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'GESTION')
    assert UserView.input_departement() == 'gestion'


def test_input_departement_invalid(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['technicien', 'gestion']):
        UserView.input_departement()
    captured = capsys.readouterr()
    print(captured)
    assert "Nom de département invalide." in captured.out


def test_input_password(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'password')
    assert UserView.input_password() == 'password'


def test_input_id_user_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1']):
        UserView.input_id_user()
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_input_password_invalid_too_small(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['mdp', 'password']):
        UserView.input_password()
    captured = capsys.readouterr()
    assert "Votre mot de passe est trop court!" in captured.out


def test_ask_user_update_field_1(monkeypatch, capsys):
    with patch('builtins.input', return_value="1"):
        assert UserView.ask_user_update_field() == "nom"


def test_ask_user_update_field_2(monkeypatch, capsys):
    with patch('builtins.input', return_value="2"):
        assert UserView.ask_user_update_field() == "departement"


def test_ask_user_update_field_3(monkeypatch, capsys):
    with patch('builtins.input', return_value="3"):
        assert UserView.ask_user_update_field() == "email"


def test_ask_user_update_field_4(monkeypatch, capsys):
    with patch('builtins.input', return_value="4"):
        assert UserView.ask_user_update_field() == "password"


def test_ask_client_update_field_invalid_no_int(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['marc', '1']):
        UserView.ask_user_update_field()

    captured = capsys.readouterr()
    assert captured.out == "ERROR: Vous n'avez pas saisi un numéro\n"


def test_ask_client_update_field_invalid(monkeypatch, capsys):
    with patch('builtins.input', side_effect=['7', '1']):
        UserView.ask_user_update_field()

    captured = capsys.readouterr()
    assert captured.out == "WARNING: Vous n'avez pas saisi un numéro valide\n"
