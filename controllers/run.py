import controllers.menu_controllers
from controllers.users_controllers import UserController
from controllers.auth_controllers import AuthController
from sqlalchemy import inspect
from models.users import User
from models.clients import Client
from models.role import Role
from config import session, engine


class RunInscription:

    def __call__(self, *args, **kwargs):
        user_controller = UserController(User)
        user_controller.add_user()
        return controllers.menu_controllers.HomeMenuController()


class RunConnexion:

    def __call__(self, *args, **kwargs):
        user_controller = UserController(User)
        name, password = user_controller.connecter_user()
        print(name)
        print("******")
        print(password)
        try:
            user = session.query(User).filter_by(name=name).first()
            print(user)
            if user and user.check_password(password):
                print("Connexion réussie !")
                user_authcontroller = AuthController(user)
                try:
                    token = user_authcontroller.generate_token()
                except Exception as token_error:
                    print(f"Une erreur s'est produite lors de la génération du token : {token_error}")
                return controllers.menu_controllers.EpicEventMenuController()
            else:
                print("Adresse e-mail ou mot de passe incorrect. Veuillez réessayer.")
                return None
        except Exception as e:
            print(f"Connexion impossible en raison d'une erreur. : {e}")
            return None


class RunBaseDeDonnee:

    def __call__(self, *args, **kwargs):
        if engine is not None:
            # Inspecter le schéma de la base de données pour voir les tables créées
            inspector = inspect(engine)
            tables = inspector.get_table_names()
            print("Tables créées :", tables)
            clients = session.query(Client).all()
            users = session.query(User).all()
            # Afficher les données
            for client in clients:
                print(client)
            for user in users:
                print(user)
        else:
            print("Erreur: Aucun moteur de base de données n'a été fourni.")

        return controllers.menu_controllers.HomeMenuController()


class RunCreateUser:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "create_user" in Role(role_decode).has_user_permissions():
                user_controller = UserController(User)  # Créer une instance de UserController avec User comme modèle
                user_controller.add_user()  # Appeler la méthode inscr
            else:
                print("Vous n'avez pas la permission de créer un utilisateur.")
        return controllers.menu_controllers.UserMenuController()


class RunDeleteUser:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "delete_user" in Role(role_decode).has_user_permissions():
                user_controller = UserController(User)  # Créer une instance de UserController avec User comme modèle
                user_controller.delete_user_by_id()  # Appeler la méthode inscr
            else:
                print("Vous n'avez pas la permission de créer un utilisateur.")
        return controllers.menu_controllers.UserMenuController()


class RunReadUser:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "read_user" in Role(role_decode).has_user_permissions():
                user_controller = UserController(User)  # Créer une instance de UserController avec User comme modèle
                user_controller.read_all_users()  # Appeler la méthode inscr
            else:
                print("Vous n'avez pas la permission de créer un utilisateur.")
        return controllers.menu_controllers.UserMenuController()
