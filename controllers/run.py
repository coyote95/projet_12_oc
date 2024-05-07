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
from sentry_sdk import capture_exception, capture_message
from functools import wraps


# Décorateur pour vérifier la connection
def login(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        controller_auth = AuthController()
        print("login")
        if controller_auth.valid_token():
            print('token valide')
            return func(self, *args, **kwargs)
        else:
            print('token invalide')
            return controllers.menu_controllers.HomeMenuController()

    return wrapper


# Décorateur pour vérifier les autorisations
def check_permissions(permissions):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            print("permission")
            if self.has_permissions(permissions):
                return func(self, *args, **kwargs)
            else:
                BaseView.display_warning_message(
                    f"Vous n'avez pas la permission d'effectuer cette action {permissions}.")
                return self.get_menu_controller()

        return wrapper

    return decorator


# Classe de base pour toutes les actions
class RunAction:
    def __init__(self):
        self.user_authcontroller = AuthController()
        self.id_user = None
        self.role_user = None

    def has_permissions(self, permissions):
        if self.user_authcontroller.valid_token():
            role_decode, id_decode = self.user_authcontroller.decode_payload_id_and_role_token()
            self.id_user = id_decode
            self.role_user = role_decode
            return all(permission in Role(role_decode).has_permissions() for permission in permissions)
        return False

    def get_menu_controller(self):
        raise NotImplementedError("La méthode get_menu_controller doit être implémentée dans la classe fille.")


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
            if user and user.check_password(password):
                capture_message(f"Utilisateur {user.id} connecté", level="info")
                BaseView.display_info_message("Connexion réussie !")
                user_authcontroller = AuthController(user)
                try:
                    user_authcontroller.generate_token()
                    return controllers.menu_controllers.EpicEventMenuController()  # id_decode,role_decode
                except Exception as token_error:
                    BaseView.display_error_message(
                        f"Une erreur s'est produite lors de la génération du token : {token_error}")

            else:
                BaseView.display_warning_message("Adresse e-mail ou mot de passe incorrect. Veuillez réessayer.")
                return controllers.menu_controllers.HomeMenuController()
        except Exception as e:
            BaseView.display_error_message(f"Connexion impossible en raison d'une erreur. : {e}")
            return None


class RunCreateUser(RunAction):
    @login
    @check_permissions(["create_user"])
    def __call__(self, *args, **kwargs):
        user_controller = UserController()
        user_controller.create_user()
        return controllers.menu_controllers.UserMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.UserMenuController()


class RunDeleteUser(RunAction):
    @login
    @check_permissions(["delete_user"])
    def __call__(self, *args, **kwargs):
        user_controller = UserController()
        user_controller.delete_user_by_id()
        return controllers.menu_controllers.UserMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.UserMenuController()


class RunReadUser(RunAction):
    @login
    @check_permissions(["read_user"])
    def __call__(self, *args, **kwargs):
        user_controller = UserController()
        user_controller.read_all_users()
        return controllers.menu_controllers.UserMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.UserMenuController()


class RunFilterUser(RunAction):
    @login
    @check_permissions(["filter_user"])
    def __call__(self, *args, **kwargs):
        user_controller = UserController()
        user_controller.filter_users()
        return controllers.menu_controllers.UserMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.UserMenuController()


class RunUpdateUser(RunAction):
    @login
    @check_permissions(["update_user"])
    def __call__(self, *args, **kwargs):
        user_controller = UserController()
        user_controller.update_user()
        return controllers.menu_controllers.UserMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.UserMenuController()


class RunCreateClient(RunAction):
    @login
    @check_permissions(["create_client"])
    def __call__(self, *args, **kwargs):
        client_controller = ClientController()
        client_controller.create_client(self.id_user)
        return controllers.menu_controllers.ClientMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.ClientMenuController()


class RunDeleteClient(RunAction):
    @login
    @check_permissions(["delete_client"])
    def __call__(self, *args, **kwargs):
        client_controller = ClientController()
        client_controller.delete_client_by_id(self.id_user)
        return controllers.menu_controllers.ClientMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.ClientMenuController()


class RunReadClient(RunAction):
    @login
    @check_permissions(["read_client"])
    def __call__(self, *args, **kwargs):
        client_controller = ClientController()
        client_controller.read_all_client()
        return controllers.menu_controllers.ClientMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.ClientMenuController()


class RunFilterClient(RunAction):
    @login
    @check_permissions(["filter_client"])
    def __call__(self, *args, **kwargs):
        client_controller = ClientController()
        client_controller.filter_client(self.role_user, self.id_user)
        return controllers.menu_controllers.ClientMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.ClientMenuController()


class RunUpdateClient(RunAction):
    @login
    @check_permissions(["update_client"])
    def __call__(self, *args, **kwargs):
        client_controller = ClientController()
        client_controller.update_client(self.id_user)
        return controllers.menu_controllers.ClientMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.ClientMenuController()


class RunCreateContract(RunAction):
    @login
    @check_permissions(["create_contract"])
    def __call__(self, *args, **kwargs):
        contract_controller = ContractController()
        contract_controller.create_contract(self.role_user, self.id_user)
        return controllers.menu_controllers.ContratsMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.ContratsMenuController()


class RunDeleteContract(RunAction):
    @login
    @check_permissions(["delete_contract"])
    def __call__(self, *args, **kwargs):
        contract_controller = ContractController()
        contract_controller.delete_contract_by_id(self.role_user, self.id_user)
        return controllers.menu_controllers.ContratsMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.ContratsMenuController()


class RunReadContract(RunAction):
    @login
    @check_permissions(["read_contract"])
    def __call__(self, *args, **kwargs):
        contract_controller = ContractController()
        contract_controller.read_all_contracts()
        return controllers.menu_controllers.ContratsMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.ContratsMenuController()


class RunFilterContract(RunAction):
    @login
    @check_permissions(["filter_contract"])
    def __call__(self, *args, **kwargs):
        contract_controller = ContractController()
        contract_controller.filter_contracts(self.role_user)
        return controllers.menu_controllers.ContratsMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.ContratsMenuController()


class RunUpdateContract(RunAction):
    @login
    @check_permissions(["update_contract"])
    def __call__(self, *args, **kwargs):
        contract_controller = ContractController()
        contract_controller.update_contract(self.role_user, self.id_user)
        return controllers.menu_controllers.ContratsMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.ContratsMenuController()


class RunCreateEvent(RunAction):
    @login
    @check_permissions(["create_event"])
    def __call__(self, *args, **kwargs):
        event_controller = EventController()
        event_controller.create_event(self.id_user)
        return controllers.menu_controllers.EvenementMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.EvenementMenuController()


class RunDeleteEvent(RunAction):
    @login
    @check_permissions(["delete_event"])
    def __call__(self, *args, **kwargs):
        event_controller = EventController()
        event_controller.create_event(self.id_user)
        return controllers.menu_controllers.EvenementMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.EvenementMenuController()


class RunReadEvent(RunAction):
    @login
    @check_permissions(["read_event"])
    def __call__(self, *args, **kwargs):
        event_controller = EventController()
        event_controller.read_all_events()
        return controllers.menu_controllers.EvenementMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.EvenementMenuController()


class RunFilterEvent(RunAction):
    @login
    @check_permissions(["filter_event"])
    def __call__(self, *args, **kwargs):
        event_controller = EventController()
        event_controller.filter_events(self.role_user, self.id_user)
        return controllers.menu_controllers.EvenementMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.EvenementMenuController()


class RunUpdateEvent(RunAction):
    @login
    @check_permissions(["update_event"])
    def __call__(self, *args, **kwargs):
        event_controller = EventController()
        event_controller.update_event(self.role_user, self.id_user)
        return controllers.menu_controllers.EvenementMenuController()

    def get_menu_controller(self):
        return controllers.menu_controllers.EvenementMenuController()


