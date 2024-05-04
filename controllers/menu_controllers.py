import sys
from models.menu import Menu
from views.menu_view import HomeMenuView
from controllers.run import (RunInscription, RunConnexion,
                             RunCreateUser, RunDeleteUser, RunReadUser, RunFilterUser, RunUpdateUser,
                             RunCreateClient, RunDeleteClient, RunReadClient, RunFilterClient, RunUpdateClient,
                             RunCreateContract, RunDeleteContract, RunReadContract, RunFilterContract,RunUpdateContract,
                             RunCreateEvent, RunDeleteEvent, RunReadEvent, RunFilterEvent, RunUpdateEvent)


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
    def __init__(self, ):
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


class QuitController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_title("Fin du programme")
        sys.exit()
