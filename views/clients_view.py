import re
from views.base_view import BaseView


class ClientView(BaseView):
    """
    Provides methods for user input and displaying client information.

    Inherits from:
        BaseView: A base class providing methods to display messages in different colors.

    Methods:
        input_name(): Prompts the user to input their name.
        input_surname(): Prompts the user to input their surname.
        input_company(): Prompts the user to input their company.
        input_phone(): Prompts the user to input their phone number.
        input_email(): Prompts the user to input their email address.
        input_id_client(): Prompts the user to input the client's ID.
        input_id_commercial(): Prompts the user to input the commercial's ID.
        input_info_client(): Prompts the user to input client information (name, surname, email, phone, company).
        display_client(client): Displays information about a client.
        ask_client_update_field(): Asks the user which field of the client they want to update.
        filter_message(message): Displays a filter message.
    """

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
            phone = input("Entrez votre numéro de téléphone:")
            if phone.isdigit() and len(phone) == 10:
                return phone
            else:
                ClientView.display_error_message(
                    "Votre numéro ne comporte pas 10 chiffres"
                )

    @staticmethod
    def input_email():
        while True:
            email = input("Entrez votre email: ")
            if re.match(r"^[\w\.-]+@[\w\.-]+$", email):
                return email
            else:
                ClientView.display_error_message(
                    "Adresse email invalide. Veuillez réessayer."
                )

    @staticmethod
    def input_id_client():
        while True:
            try:
                client_id = int(input("Entrez l'id du client: "))
                return client_id
            except ValueError:
                ClientView.display_error_message("Vous n'avez pas saisi un numéro")

    @staticmethod
    def input_id_commercial():
        while True:
            try:
                commercial_id = int(input("Entrez l'id du commercial: "))
                return commercial_id
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
                choice = int(
                    input(
                        f"Quelle information voulez-vous modifier?\n"
                        f"1: Nom\n"
                        f"2: Prénom\n"
                        f"3: Email\n"
                        f"4: Téléphone\n"
                        f"5: Entreprise\n"
                        f"6: Commercial\n"
                    )
                )
                if choice == 1:
                    return "nom"
                elif choice == 2:
                    return "prenom"
                elif choice == 3:
                    return "email"
                elif choice == 4:
                    return "telephone"
                elif choice == 5:
                    return "entreprise"
                elif choice == 6:
                    return "commercial"
                else:
                    ClientView.display_warning_message(
                        "Vous n'avez pas saisi un numéro valide"
                    )

            except ValueError:
                ClientView.display_error_message("Vous n'avez pas saisi un numéro")

    @staticmethod
    def filter_message(message):
        print(message)
