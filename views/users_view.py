import re
from views.base_view import BaseView


class UserView(BaseView):

    @staticmethod
    def input_name():
        name = input("Entrez votre nom: ")
        return name.upper()

    @staticmethod
    def input_email():
        while True:
            email = input("Entrez votre email: ")
            # Expression régulière pour valider le format de l'email
            if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                return email
            else:
                BaseView.display_error_message("Adresse email invalide. Veuillez réessayer.")

    @staticmethod
    def input_departement():
        while True:
            departement = input("Entrez votre département (gestion, commercial, support) : ")
            if departement.lower() in ["gestion", "commercial", "support"]:
                return departement.lower()
            else:
                UserView.display_error_message("Nom de département invalide. Veuillez indiquer :"
                                               " 'gestion', 'support' ou 'commercial'")

    @staticmethod
    def input_password():
        while True:
            password = input("Entrez votre mot de passe (8 caractères min) : ")
            if len(password) >= 8:
                return password
            else:
                UserView.display_error_message("Votre mot de passe est trop court!")

    @staticmethod
    def input_id_user():
        while True:
            user_id = input("Entrez l'id de l'utilisateur: ")
            try:
                user_id = int(user_id)
                return user_id
            except ValueError:
                UserView.display_error_message("Vous n'avez pas saisi un numéro")


    @staticmethod
    def ask_infos_user_login():
        name = UserView.input_name()
        password = UserView.input_password()
        return name, password

    @staticmethod
    def input_infos_user():
        name = UserView.input_name()
        email = UserView.input_email()
        departement = UserView.input_departement()
        password = UserView.input_password()
        return name, email, departement, password

    @staticmethod
    def display_user(user):
        print(
            f"id:{user.get_id()}    "
            f"Nom:{user.get_name()}    "
            f"Email:{user.get_email()}    "
            f"Departement:{user.get_departement()}    "
            f"clients:{user.get_clients_name()}    "
        )

    @staticmethod
    def ask_user_update_field():
        while True:
            try:
                choice = int(input(
                    f"Quelle information voulez-vous modifier?\n"
                    f"1: Nom\n"
                    f"2: Département\n"
                    f"3: Email\n"
                    f"4: Password\n"
                ))
                if choice == 1:
                    return "nom"
                elif choice == 2:
                    return "departement"
                elif choice == 3:
                    return "email"
                elif choice == 4:
                    return "password"
                else:
                    UserView.display_warning_message("Vous n'avez pas saisi un numéro valide")

            except ValueError:
                UserView.display_error_message("Vous n'avez pas saisi un numéro")

