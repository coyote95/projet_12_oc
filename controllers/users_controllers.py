from views.users_view import UserView
from settings.database import session
from models.users import User


class UserController:
    def __init__(self):
        self.model = User
        self.view = UserView()

    def create_user(self):
        name, email, departement, password = self.view.input_infos_user()
        new_user = self.model(name=name, email=email, password=password, departement=departement)
        session.add(new_user)
        session.commit()
        self.view.display_info_message("Inscription réussie !")
        return new_user

    def delete_user_by_id(self):
        user_id = self.view.input_id_user()
        user = self.model.filter_by_id(user_id)
        if user:
            session.delete(user)
            session.commit()
            self.view.display_info_message("Utilisateur supprimé avec succès.")
        else:
            self.view.display_warning_message("Utilisateur non trouvé.")

    def connecter_user(self):
        name, password = self.view.ask_infos_user_login()
        return name, password

    def read_all_users(self):
        try:
            users = self.model.filter_all_users()
            if users:
                for user in users:
                    self.view.display_user(user)
            else:
                self.view.display_warning_message("Aucun utilisateur trouvé.")
        except Exception as e:
            self.view.display_error_message(f"Une erreur s'est produite lors de la récupération "
                                            f"des utilisateurs : {e}")

    def filter_users(self):
        self.view.display_info_message("Aucun filtre utilisateur disponible")

    def update_user(self):
        user_id = self.view.input_id_user()
        user = self.model.filter_by_id(user_id)
        if user:
            self.view.display_user(user)
            choice = self.view.ask_user_update_field()

            if choice == "nom":
                new_name = self.view.input_name()
                user.set_name(new_name)
                session.commit()
                self.view.display_info_message("Nom de l'utilisateur modifié avec succès.")

            elif choice == "departement":
                new_departement = self.view.input_departement()
                user.set_departement(new_departement)
                user.set_role_from_departement()
                session.commit()
                self.view.display_info_message("Département de l'utilisateur modifié avec succès.")

            elif choice == "email":
                new_email = self.view.input_email()
                user.set_email(new_email)
                session.commit()
                self.view.display_info_message("Email de l'utilisateur modifié avec succès.")

            elif choice == "password":
                new_password = self.view.input_password()
                user.set_password(new_password)
                session.commit()
                self.view.display_info_message("Password de l'utilisateur modifié avec succès.")
            else:
                self.view.display_error_message("Option invalide.")
