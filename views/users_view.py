import re


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
    def input_id_user_delete():
        while True:
            user_id = input("Entrez l'id du user à supprimer: ")
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
