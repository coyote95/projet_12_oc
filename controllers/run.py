import controllers.menu_controllers
from controllers.users_controllers import UserController
from controllers.clients_controllers import ClientController
from controllers.contract_controllers import ContractController
from controllers.event_controllers import EventController
from controllers.auth_controllers import AuthController
from views.base_view import BaseView
from models.users import User
from models.role import Role
from settings.database import session


class RunInscription:

    def __call__(self, *args, **kwargs):
        user_controller = UserController()
        user_controller.create_user()
        return controllers.menu_controllers.HomeMenuController()


class RunConnexion:

    def __call__(self, *args, **kwargs):
        user_controller = UserController()
        name, password = user_controller.connecter_user()
        try:
            user = session.query(User).filter_by(name=name).first()
            print(user)
            if user and user.check_password(password):
                BaseView.display_info_message("Connexion réussie !")
                user_authcontroller = AuthController(user)
                try:
                    user_authcontroller.generate_token()
                    return controllers.menu_controllers.EpicEventMenuController()
                except Exception as token_error:
                    BaseView.display_error_message(
                        f"Une erreur s'est produite lors de la génération du token : {token_error}")

            else:
                BaseView.display_warning_message("Adresse e-mail ou mot de passe incorrect. Veuillez réessayer.")
                return controllers.menu_controllers.HomeMenuController()
        except Exception as e:
            BaseView.display_error_message(f"Connexion impossible en raison d'une erreur. : {e}")
            return None


class RunCreateUser:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "create_user" in Role(role_decode).has_user_permissions():
                user_controller = UserController()
                user_controller.create_user()
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de créer un utilisateur.")
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
                BaseView.display_warning_message("Vous n'avez pas la permission de supprimer un utilisateur.")
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
                BaseView.display_warning_message("Vous n'avez pas la permission de lire un utilisateur.")
        return controllers.menu_controllers.UserMenuController()


class RunFilterUser:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "filter_user" in Role(role_decode).has_user_permissions():
                user_controller = UserController()
                user_controller.filter_users()
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de filter les utilisateurs.")
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
                BaseView.display_warning_message("Vous n'avez pas la permission de modifier un utilisateur.")
        return controllers.menu_controllers.UserMenuController()


class RunCreateClient:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "create_client" in Role(role_decode).has_client_permissions():
                client_controller = ClientController()
                client_controller.create_client(id_decode)
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de créer un client.")
        return controllers.menu_controllers.ClientMenuController()


class RunDeleteClient:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "delete_client" in Role(role_decode).has_client_permissions():
                client_controller = ClientController()
                client_controller.delete_client_by_id(id_decode)
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de supprimer un client.")
        return controllers.menu_controllers.ClientMenuController()


class RunReadClient:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "read_client" in Role(role_decode).has_client_permissions():
                client_controller = ClientController()
                client_controller.read_all_client()
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de lire un client.")
        return controllers.menu_controllers.ClientMenuController()


class RunFilterClient:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "filter_client" in Role(role_decode).has_client_permissions():
                client_controller = ClientController()
                client_controller.filter_client(role_decode,id_decode)
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de filtrer les clients.")
        return controllers.menu_controllers.ClientMenuController()


class RunUpdateClient:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "update_client" in Role(role_decode).has_client_permissions():
                client_controller = ClientController()
                client_controller.update_client(id_decode)
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de modifier un client.")
        return controllers.menu_controllers.ClientMenuController


class RunCreateContract:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "create_contract" in Role(role_decode).has_contract_permissions():
                contract_controller = ContractController()
                contract_controller.create_contract(role_decode, id_decode)
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de créer un contrat.")
        return controllers.menu_controllers.ContratsMenuController()


class RunDeleteContract:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "delete_contract" in Role(role_decode).has_contract_permissions():
                contract_controller = ContractController()
                contract_controller.delete_contract_by_id(role_decode, id_decode)
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de supprimer un contrat.")
        return controllers.menu_controllers.ContratsMenuController


class RunReadContract:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "read_contract" in Role(role_decode).has_contract_permissions():
                contract_controller = ContractController()
                contract_controller.read_all_contracts()
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de lire un contrat.")
        return controllers.menu_controllers.ContratsMenuController()


class RunFilterContract:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "filter_contract" in Role(role_decode).has_contract_permissions():
                contract_controller = ContractController()
                contract_controller.filter_contracts(role_decode)
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de filtrer les contacts.")
        return controllers.menu_controllers.ContratsMenuController()


class RunUpdateContract:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "update_contract" in Role(role_decode).has_contract_permissions():
                contract_controller = ContractController()
                contract_controller.update_contract(role_decode, id_decode)
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de modifier un contrat.")
        return controllers.menu_controllers.ContratsMenuController


class RunCreateEvent:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "create_event" in Role(role_decode).has_event_permissions():
                event_controller = EventController()
                event_controller.create_event(id_decode)
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de créer un contrat.")
        return controllers.menu_controllers.EvenementMenuController()


class RunDeleteEvent:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "delete_event" in Role(role_decode).has_event_permissions():
                event_controller = EventController()
                event_controller.delete_event_by_id(id_decode)
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de supprimer un evenement.")
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
                BaseView.display_warning_message("Vous n'avez pas la permission de lire un événement.")
        return controllers.menu_controllers.EvenementMenuController()


class RunFilterEvent:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode = user_authcontroller.decode_payload_role_token(token)
            if "filter_event" in Role(role_decode).has_event_permissions():
                event_controller = EventController()
                event_controller.filter_events()
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de filtrer les événements.")
        return controllers.menu_controllers.EvenementMenuController()


class RunUpdateEvent:

    def __call__(self, *args, **kwargs):
        user_authcontroller = AuthController()
        token = user_authcontroller.read_token()

        if token:
            role_decode, id_decode = user_authcontroller.decode_payload_id_role_token(token)
            if "update_event" in Role(role_decode).has_event_permissions():
                event_controller = EventController()
                event_controller.update_event(role_decode, id_decode)
            else:
                BaseView.display_warning_message("Vous n'avez pas la permission de modifier un événement.")
        return controllers.menu_controllers.ContratsMenuController
