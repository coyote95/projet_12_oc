import sys
from models.menu import Menu
from views.menu_view import HomeMenuView
from controllers.auth_controllers import AuthController
from controllers.run import (RunInscription, RunConnexion,
                             RunCreateUser, RunDeleteUser, RunReadUser, RunFilterUser, RunUpdateUser,
                             RunCreateClient, RunDeleteClient, RunReadClient, RunFilterClient, RunUpdateClient,
                             RunCreateContract, RunDeleteContract, RunReadContract, RunFilterContract,
                             RunUpdateContract,
                             RunCreateEvent, RunDeleteEvent, RunReadEvent, RunFilterEvent, RunUpdateEvent)
from sentry_sdk import capture_exception, capture_message
from functools import wraps


# def login(func):
#     print("test")
#
#     @wraps(func)
#     def wrapper():
#         controller_auth = AuthController()
#
#         if controller_auth.valid_token():
#             print('wrap')
#             return func()
#         else:
#             return HomeMenuController()
#
#     return wrapper


class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()


class HomeMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_title("EPIC EVENTS")
        self.menu.add("auto", "Connexion", RunConnexion())
        self.menu.add("auto", "Inscription", RunInscription())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class EpicEventMenuController:
    def __init__(self):
        self.id_decode = None
        self.role_decode = None
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_title("Menu Principal")
        self.menu.add("auto", "Utilisateurs", UserMenuController())
        self.menu.add("auto", "Clients", ClientMenuController())
        self.menu.add("auto", "Contrats", ContratsMenuController())
        self.menu.add("auto", "Evenements", EvenementMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class UserMenuController:
    def __init__(self):
        self.id_decode = None
        self.role_decode = None
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_title("Menu Utilisateurs")
        self.menu.add("auto", "Lire", RunReadUser())
        self.menu.add("auto", "Filtrer", RunFilterUser())
        self.menu.add("auto", "Creer", RunCreateUser())
        self.menu.add("auto", "Modifier", RunUpdateUser())
        self.menu.add("auto", "Supprimer", RunDeleteUser())
        self.menu.add("r", "Retour", EpicEventMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class ClientMenuController:
    def __init__(self, ):
        self.id_decode = None
        self.role_decode = None
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_title("Menu Clients")
        self.menu.add("auto", "Lire", RunReadClient())
        self.menu.add("auto", "Filtrer", RunFilterClient())
        self.menu.add("auto", "Creer", RunCreateClient())
        self.menu.add("auto", "Modifier", RunUpdateClient())
        self.menu.add("auto", "Supprimer", RunDeleteClient())
        self.menu.add("r", "Retour", EpicEventMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class ContratsMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_title("Menu Contrats")
        self.menu.add("auto", "Lire", RunReadContract())
        self.menu.add("auto", "Filter", RunFilterContract())
        self.menu.add("auto", "Creer", RunCreateContract())
        self.menu.add("auto", "Modifier", RunUpdateContract())
        self.menu.add("auto", "Supprimer", RunDeleteContract())
        self.menu.add("r", "Retour", EpicEventMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class EvenementMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_title("Menu Evenements")
        self.menu.add("auto", "Lire", RunReadEvent())
        self.menu.add("auto", "Filtrer", RunFilterEvent())
        self.menu.add("auto", "Creer", RunCreateEvent())
        self.menu.add("auto", "Modifier", RunUpdateEvent())
        self.menu.add("auto", "Supprimer", RunDeleteEvent())
        self.menu.add("r", "Retour", EpicEventMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class QuitController:# quitter si user_id different de 0 ne pas faire de lecture de token
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        if user_authcontroller.valid_token():
            role_decode, id_decode = user_authcontroller.decode_payload_id_and_role_token()
            capture_message(f"Utilisateur {id_decode} déconnecté", level="info")
        self.view.display_title("Fin du programme")
        sys.exit()
