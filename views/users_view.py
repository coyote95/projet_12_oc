import re
from models.users import UserField


class UserView:

    @staticmethod
    def afficher_message(message):
        print(message)

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
                print("Adresse email invalide. Veuillez réessayer.")

    @staticmethod
    def input_departement():
        while True:
            departement = input("Entrez votre département (gestion, commercial, support) : ")
            if departement.lower() in ["gestion", "commercial", "support"]:
                return departement.lower()
            else:
                print("Nom de département invalide. Veuillez indiquer : 'gestion', 'support' ou 'commercial'")

    @staticmethod
    def input_password():
        while True:
            password = input("Entrez votre mot de passe (8 caractères min) : ")
            if len(password) >= 8:
                return password
            else:
                print("Votre mot de passe est trop court!")

    @staticmethod
    def input_id_user():
        while True:
            user_id = input("Entrez l'id de l'user: ")
            try:
                user_id = int(user_id)
                return user_id
            except ValueError:
                print("Vous n'avez pas écrit un entier.")

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
            f"Departement:{user.get_departement()}    "
            f"clients:{user.get_clients_name()}    "
        )  # add clients

    @staticmethod
    def ask_user_update_field():
        while True:
            try:
                choice = int(input(
                    f"Quelle information voulez-vous modifier?\n"
                    f"1: {UserField.NOM.name}\n"
                    f"2: {UserField.DEPARTEMENT.name}\n"
                    f"3: {UserField.CLIENTS.name}\n"
                ))
                field = UserField(choice)
                if field in UserField:
                    return field
                else:
                    print("Vous n'avez pas écrit un numéro valide.")
            except ValueError:
                print("Vous devez entrer un entier.")
