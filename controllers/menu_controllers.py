import sys
from models.menu import Menu
from views.menu_view import HomeMenuView
from controllers.run import (RunInscription, RunBaseDeDonnee, RunConnexion, RunCreateUser,RunDeleteUser,RunReadUser,
                             RunUpdateUser,RunCreateClient, RunDeleteClient, RunReadClient, RunUpdateClient)


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
        self.view.display_message_accueil()
        self.menu.add("auto", "Connexion", RunConnexion())
        self.menu.add("auto", "Inscription", RunInscription())
        self.menu.add("auto", "Base de donnée", RunBaseDeDonnee())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class EpicEventMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        print("*** menu principal ***")
        self.menu.add("auto", "User", UserMenuController())
        self.menu.add("auto", "Client", ClientMenuController())
        self.menu.add("auto", "Contrat", ContratsMenuController())
        self.menu.add("auto", "Evenement", EvenementMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class UserMenuController:
    def __init__(self, ):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        print("***  Menu User   ***")
        self.menu.add("auto", "Lire", RunReadUser())
        self.menu.add("auto", "Creer", RunCreateUser())
        self.menu.add("auto", "Modifier", RunUpdateUser())
        self.menu.add("auto", "Supprimer", RunDeleteUser())
        self.menu.add("r", "Retour", EpicEventMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class ClientMenuController:
    def __init__(self, ):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        print("***  Menu Client   ***")
        self.menu.add("auto", "Lire", RunReadClient())
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
        print("***  Menu Contrats   ***")
        self.menu.add("auto", "Lire", None)
        self.menu.add("auto", "Creer", None)
        self.menu.add("auto", "Modifier", None)
        self.menu.add("auto", "Supprimer", None)
        self.menu.add("r", "Retour", EpicEventMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class EvenementMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        print("***  Menu Evenements   ***")
        self.menu.add("auto", "Lire", None)
        self.menu.add("auto", "Creer", None)
        self.menu.add("auto", "Modifier", None)
        self.menu.add("auto", "Supprimer", None)
        self.menu.add("r", "Retour", EpicEventMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class QuitController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_message_end_programme()
        sys.exit()
