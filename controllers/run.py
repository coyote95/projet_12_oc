from controllers.clients_controllers import ClientController
from sqlalchemy import inspect
from views.clients_view import ClientView
import controllers.menu_controllers
from models.clients import Client
import sqlalchemy


class RunInscription:
    def __init__(self, session,engine):
        self.controller = ClientController(session)
        self.view = ClientView()
        self.session = session
        self.engine=engine

    def __call__(self, *args, **kwargs):
        nom_complet, email, telephone, entreprise = self.view.demander_infos_client()
        self.controller.inscrire_client(nom_complet, email, telephone, entreprise)
        return controllers.menu_controllers.HomeMenuController(self.session, self.engine)


class RunBaseDeDonnee:
    def __init__(self,session, engine=None):
        self.engine = engine
        self.session = session

    def __call__(self, *args, **kwargs):
        if self.engine is not None:
            # Inspecter le schéma de la base de données pour voir les tables créées
            inspector = inspect(self.engine)
            tables = inspector.get_table_names()
            print("Tables créées :", tables)

            clients = self.session.query(Client).all()
            # Afficher les données
            for client in clients:
                print(client)

        else:
            print("Erreur: Aucun moteur de base de données n'a été fourni.")

