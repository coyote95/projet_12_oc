import re
from models.clients import ClientField
from views.base_view import BaseView


class ClientView(BaseView):

    @staticmethod
    def afficher_message(message):
        print(message)

    @staticmethod
    def input_name():
        name = input("Entrez votre nom: ")
        return name.upper()

    @staticmethod
    def input_surname():
        name = input("Entrez votre prénom: ")
        return name.upper()

    @staticmethod
    def input_company():
        name = input("Entrez votre entreprise: ")
        return name.lower()

    @staticmethod
    def input_phone():
        while True:
            try:
                phone = input("Entrez votre numéro de téléphone:")
                if len(phone) == 10 and phone.isdigit():
                    return int(phone)
                else:
                    ClientView.display_error_message("Votre numéro ne comporte pas 10 chiffres")
            except ValueError:
                ClientView.display_error_message("Vous n'avez pas saisi un numéro")

    @staticmethod
    def input_email():
        while True:
            email = input("Entrez votre email: ")
            # Expression régulière pour valider le format de l'email
            if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                return email
            else:
                ClientView.display_error_message("Adresse email invalide. Veuillez réessayer.")


    @staticmethod
    def input_id_client():
        while True:
            client_id = input("Entrez l'id du client: ")
            try:
                client_id = int(client_id)
                return client_id
            except ValueError:
                ClientView.display_error_message("Vous n'avez pas saisi un numéro")

    @staticmethod
    def input_info_client():
        name = ClientView.input_name()
        surname = ClientView.input_surname()
        email = ClientView.input_email()
        phone = ClientView.input_phone()
        company = ClientView.input_company()
        return name, surname, email, phone, company

    @staticmethod
    def display_client(client):
        print(
            f"id:{client.get_id()}    "
            f"Nom:{client.get_name()}    "
            f"Prénom:{client.get_surname()}    "
            f"Email:{client.get_email()}    "
            f"Telephone:{client.get_phone()}    "
            f"Entreprise:{client.get_company()}    "
            f"Date creation:{client.get_creation_date()}    "
            f"Date mise à jour:{client.get_last_update_date()}    "
            f"Commercial:{client.get_user_name()}    "
        )

    @staticmethod
    def ask_client_update_field():
        while True:
            try:
                choice = int(input(
                    f"Quelle information voulez-vous modifier?\n"
                    f"1: {ClientField.NOM.name}\n"
                    f"2: {ClientField.SURNAME.name}\n"
                    f"3: {ClientField.EMAIL.name}\n"
                    f"4: {ClientField.PHONE.name}\n"
                    f"5: {ClientField.COMPANY.name}\n"
                ))
                field = ClientField(choice)
                if field in ClientField:
                    return field
                else:
                    ClientView.display_error_message("Vous n'avez pas saisi un numéro valide")
            except ValueError:
                ClientView.display_error_message("Vous n'avez pas saisi un numéro")
