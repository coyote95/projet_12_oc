import controllers.menu_controllers
from controllers.users_controllers import UserController
from controllers.clients_controllers import ClientController
from controllers.contract_controllers import ContractController
from controllers.event_controllers import EventController
from controllers.auth_controllers import AuthController
from sqlalchemy import inspect
from models.users import User
from models.clients import Client
from models.role import Role
from models.contract import Contract
from settings.database import session, engine


class RunInscription:

    def __call__(self, *args, **kwargs):
        user_controller = UserController()
        user_controller.add_user()
        return controllers.menu_controllers.HomeMenuController()


class RunConnexion:

    def __call__(self, *args, **kwargs):
        user_controller = UserController()
        name, password = user_controller.connecter_user()
        try:
            user = session.query(User).filter_by(name=name).first()
            print(user)
            if user and user.check_password(password):
                print("Connexion réussie !")
                user_authcontroller = AuthController(user)
                try:
                    user_authcontroller.generate_token()
                    return controllers.menu_controllers.EpicEventMenuController()
                except Exception as token_error:
                    print(f"Une erreur s'est produite lors de la génération du token : {token_error}")

            else:
                print("Adresse e-mail ou mot de passe incorrect. Veuillez réessayer.")
                return controllers.menu_controllers.HomeMenuController()
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
                user_controller = UserController()
                user_controller.add_user()
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
                user_controller = UserController()
                user_controller.delete_user_by_id()
            else:
                print("Vous n'avez pas la permission de supprimer un utilisateur.")
        return controllers.menu_controllers.UserMenuController()


class RunReadUser:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "read_user" in Role(role_decode).has_user_permissions():
                user_controller = UserController()
                user_controller.read_all_users()
            else:
                print("Vous n'avez pas la permission de lire un utilisateur.")
        return controllers.menu_controllers.UserMenuController()


class RunUpdateUser:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "update_user" in Role(role_decode).has_user_permissions():
                user_controller = UserController()
                user_controller.update_user()
            else:
                print("Vous n'avez pas la permission de modifier un utilisateur.")
        return controllers.menu_controllers.UserMenuController()


class RunCreateClient:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "create_client" in Role(role_decode).has_client_permissions():
                client_controller = ClientController(Client)
                client_controller.add_client(id_decode)
            else:
                print("Vous n'avez pas la permission de créer un client.")
        return controllers.menu_controllers.ClientMenuController()


class RunDeleteClient:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "delete_client" in Role(role_decode).has_client_permissions():
                client_controller = ClientController(Client)
                client_controller.delete_client_by_id(id_decode)
            else:
                print("Vous n'avez pas la permission de supprimer un client.")
        return controllers.menu_controllers.ClientMenuController()


class RunReadClient:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "read_client" in Role(role_decode).has_client_permissions():
                client_controller = ClientController(Client)
                client_controller.read_all_client()
            else:
                print("Vous n'avez pas la permission de lire un client.")
        return controllers.menu_controllers.ClientMenuController()


class RunUpdateClient:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "update_client" in Role(role_decode).has_client_permissions():
                client_controller = ClientController(Client)
                client_controller.update_client(id_decode)
            else:
                print("Vous n'avez pas la permission de modifier un client.")
        return controllers.menu_controllers.ClientMenuController


class RunCreateContract:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "create_contract" in Role(role_decode).has_contract_permissions():
                contract_controller = ContractController(Contract)
                contract_controller.add_contract(role_decode, id_decode)
            else:
                print("Vous n'avez pas la permission de créer un contrat.")
        return controllers.menu_controllers.ContratsMenuController()


class RunDeleteContract:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "delete_contract" in Role(role_decode).has_contract_permissions():
                contract_controller = ContractController(Contract)
                contract_controller.delete_contract_by_id(role_decode, id_decode)
            else:
                print("Vous n'avez pas la permission de supprimer un contrat.")
        return controllers.menu_controllers.ContratsMenuController


class RunReadContract:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "read_contract" in Role(role_decode).has_contract_permissions():
                contract_controller = ContractController(Contract)
                contract_controller.read_all_contracts()
            else:
                print("Vous n'avez pas la permission de lire un contrat.")
        return controllers.menu_controllers.ContratsMenuController()


class RunUpdateContract:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "update_contract" in Role(role_decode).has_contract_permissions():
                contract_controller = ContractController(Contract)
                contract_controller.update_contract(role_decode, id_decode)
            else:
                print("Vous n'avez pas la permission de modifier un contrat.")
        return controllers.menu_controllers.ContratsMenuController


class RunCreateEvent:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "create_event" in Role(role_decode).has_event_permissions():
                event_controller = EventController()
                event_controller.add_event(role_decode, id_decode)
            else:
                print("Vous n'avez pas la permission de créer un contrat.")
        return controllers.menu_controllers.EvenementMenuController()


class RunDeleteEvent:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "delete_event" in Role(role_decode).has_event_permissions():
                event_controller = EventController()
                event_controller.delete_event_by_id(role_decode, id_decode)
            else:
                print("Vous n'avez pas la permission de supprimer un evenement.")
        return controllers.menu_controllers.EvenementMenuController


class RunReadEvent:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "read_event" in Role(role_decode).has_event_permissions():
                event_controller = EventController()
                event_controller.read_all_events()
            else:
                print("Vous n'avez pas la permission de lire un événement.")
        return controllers.menu_controllers.EvenementMenuController()
