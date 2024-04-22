import controllers.menu_controllers
from controllers.users_controllers import UserController
from sqlalchemy import inspect
from models.users import User
from models.clients import Client


class RunInscription:
    def __init__(self, session, engine):
        self.session = session
        self.engine = engine

    def __call__(self, *args, **kwargs):
        user_controller = UserController(User)  # Créer une instance de UserController avec User comme modèle
        new_user = user_controller.inscription_user()  # Appeler la méthode inscr
        self.session.add(new_user)
        self.session.commit()
        return controllers.menu_controllers.HomeMenuController(self.session, self.engine)


class RunConnexion:
    def __init__(self, session, engine):
        self.session = session
        self.engine = engine

    def __call__(self, *args, **kwargs):
        user_controller = UserController(User)  # Créer une instance de UserController avec User comme modèle
        name, password = user_controller.connecter_user()  # Appeler la méthode inscr
        try:
            user = self.session.query(User).filter_by(name=name).first()
            if user and user.check_password(password):
                print("Connexion réussie !")
                return controllers.menu_controllers.EpicEventMenuController(self.session, self.engine)
            else:
                print("Adresse e-mail ou mot de passe incorrect. Veuillez réessayer.")
                return None
        except Exception as e:
            print(f"Une erreur s'est produite lors de la recherche de l'utilisateur : {e}")
            print("Connexion impossible en raison d'une erreur.")
            return None


class RunBaseDeDonnee:
    def __init__(self, session, engine=None):
        self.engine = engine
        self.session = session

    def __call__(self, *args, **kwargs):
        if self.engine is not None:
            # Inspecter le schéma de la base de données pour voir les tables créées
            inspector = inspect(self.engine)
            tables = inspector.get_table_names()
            print("Tables créées :", tables)

            clients = self.session.query(Client).all()
            users = self.session.query(User).all()
            # Afficher les données
            for client in clients:
                print(client)

            for user in users:
                print(user)

        else:
            print("Erreur: Aucun moteur de base de données n'a été fourni.")

        return controllers.menu_controllers.HomeMenuController(self.session, self.engine)
