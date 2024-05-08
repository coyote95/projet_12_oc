# from unittest.mock import patch
# import models.users
# from settings.database import numero
# from models.users import Calcul
#
# # Test pour vérifier que le patch fonctionne bien
# def test_patch_works():
#     with patch('models.users.numero', 100):
#         # Vérifiez que le patch est appliqué en imprimant la valeur de la variable globale
#         print(numero)  # Devrait imprimer 100
#         assert models.users.numero == 100
#
# # Test pour vérifier que la variable globale mockée est utilisée correctement
# def test_function_using_global_variable():
#     with patch('models.users.numero', 100):
#         # Appelez la fonction ou le code qui utilise la variable globale
#         result = Calcul.add_1()
#         # Vérifiez que la fonction retourne le résultat attendu en utilisant la variable globale mockée
#         assert result == 101
