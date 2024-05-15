from controllers import ClientController
from views.clients_view import ClientView
from models import Client, User
from unittest.mock import MagicMock, patch, Mock
from views import ContractView
from controllers.auth_controllers import AuthController
from datetime import datetime, timedelta, timezone


def test_store_token():
    with patch('builtins.open') as mock_open:
        mock_file = mock_open.return_value.__enter__.return_value
        auth_controller = AuthController()
        auth_controller.store_token("mock_token")
        mock_file.write.assert_called_once_with("mock_token")


def test_store_token_io_error(capsys):
    with patch('builtins.open') as mock_open:
        mock_file = MagicMock()
        mock_file.write.side_effect = IOError()
        mock_open.return_value.__enter__.return_value = mock_file
        auth_controller = AuthController()
        auth_controller.store_token("mock_token")
        captured = capsys.readouterr()
        assert "Erreur lors de l'écriture du fichier .token" in captured.out


def test_read_token_valid():
    file_content = "mock_token"
    with patch('builtins.open') as mock_open:
        mock_open.return_value.__enter__.return_value.read = Mock(return_value=file_content)
        auth_controller = AuthController()
        token = auth_controller.read_token()
        assert token == "mock_token"


def test_read_token_io_error(capsys):
    with patch('builtins.open') as mock_open:
        mock_open.side_effect = IOError()
        auth_controller = AuthController()
        token = auth_controller.read_token()
        captured = capsys.readouterr()
        assert "Erreur lors de la lecture du fichier .token" in captured.out
        assert token is None


def test_generate_token_valid(init_session):
    session = init_session
    expiration_time = datetime(2024, 12, 30, 12, 30, 00)
    user = User("marc", "marc@test.com", "commercial", "password")
    session.add(user)
    session.commit()

    with patch('controllers.auth_controllers.AuthController.store_token') as mock_store_token:
        with patch('jwt.encode') as mock_encode:
            # Définir le comportement de jwt.encode pour retourner un vrai jeton
            mock_encode.return_value = b"token"
            auth_controller = AuthController(user)
            token = auth_controller.generate_token()
            mock_store_token.assert_called_once_with(b"token")
            assert token == b"token"


def test_valid_token_valid_token():
    # Création d'une instance de AuthController
    auth_controller = AuthController()

    # Mock de la méthode read_token pour retourner un token valide
    with patch.object(auth_controller, 'read_token') as mock_read_token:
        mock_read_token.return_value = "valid_token"

        # Mock de jwt.decode pour retourner un payload
        with patch('jwt.decode') as mock_decode:
            mock_decode.return_value = {'user_id': 1, 'username': 'test_user'}

            # Appel de la méthode valid_token
            result = auth_controller.valid_token()

            # Vérification que le résultat est le payload décodé
            assert result == {'user_id': 1, 'username': 'test_user'}
