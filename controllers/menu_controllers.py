import sys

from models.menu import Menu
from views.menu_view import HomeMenuView
from controllers.run import RunInscription, RunBaseDeDonnee


class ApplicationController:
    def __init__(self, session,engine):
        self.controller = None
        self.session = session
        self.engine = engine

    def start(self):
        self.controller = HomeMenuController(self.session, self.engine)
        while self.controller:
            self.controller = self.controller()


class HomeMenuController:
    def __init__(self, session,engine):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.session = session
        self.engine = engine

    def __call__(self, *args, **kwargs):
        self.view.display_message_accueil()
        self.menu.add("auto", "Connexion", None)
        self.menu.add("auto", "Inscription", RunInscription(self.session,self.engine))
        self.menu.add("auto", "Base de donnée", RunBaseDeDonnee(self.session, self.engine))
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
