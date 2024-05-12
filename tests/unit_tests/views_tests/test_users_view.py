# from unittest.mock import patch
# def test_input_phone_invalid_should_return_none(monkeypatch, capsys):
#
#     with patch('builtins.input', side_effect=['123456', '1234567890']):
#         ClientView.input_phone()
#
#     captured = capsys.readouterr()
#     assert captured.out == "ERROR: Votre numéro ne comporte pas 10 chiffres\n"