import sys

from models.menu import Menu
from views.menu_view import HomeMenuView
from controllers.run import RunInscription, RunBaseDeDonnee, RunConnexion


class ApplicationController:
    def __init__(self, session, engine):
        self.controller = None
        self.session = session
        self.engine = engine

    def start(self):
        self.controller = HomeMenuController(self.session, self.engine)
        while self.controller:
            self.controller = self.controller()


class HomeMenuController:
    def __init__(self, session, engine):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.session = session
        self.engine = engine

    def __call__(self, *args, **kwargs):
        self.view.display_message_accueil()
        self.menu.add("auto", "Connexion", RunConnexion(self.session, self.engine))
        self.menu.add("auto", "Inscription", RunInscription(self.session, self.engine))
        self.menu.add("auto", "Base de donnée", RunBaseDeDonnee(self.session, self.engine))
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class EpicEventMenuController:
    def __init__(self, session, engine):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.session = session
        self.engine = engine

    def __call__(self, *args, **kwargs):
        self.menu.add("auto", "Client", None)
        self.menu.add("auto", "Contrat", None)
        self.menu.add("auto", "Evenement", None)
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
