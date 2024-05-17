"""
ClientController module for managing client-related operations.

Classes:
    ClientController: Manages client operations and interactions with the database and view.

Methods:
    __init__(self):
        Initializes the ClientController with a Client model and ClientView.

    create_client(self, user_id):
        Creates a new client with user input and associates it with the specified user.

    delete_client_by_id(self, user_id):
        Deletes a client by ID if the client is associated with the specified user.

    read_all_client(self):
        Retrieves and displays all clients from the database.

    filter_client(self, user_role, user_id):
        Filters clients based on the user's role and displays them.

    update_client(self, user_id):
        Updates client information based on user input if the client is associated with the specified user.
"""

from views import ClientView
from models import Client, User
from settings.database import session
from sentry_sdk import capture_message


class ClientController:
    def __init__(self):
        self.model = Client
        self.view = ClientView()

    def create_client(self, user_id):
        name, surname, email, phone, company = self.view.input_info_client()
        new_client = self.model(
            name=name, surname=surname, email=email, phone=phone, company=company
        )
        new_client.set_commercial_id(user_id)
        session.add(new_client)
        session.commit()
        capture_message(f"Création client:{new_client.id}", level="info")
        self.view.display_info_message("Création client réussite !")
        return new_client

    def delete_client_by_id(self, user_id):
        client_id = self.view.input_id_client()
        client = self.model.filter_by_id(client_id)
        if client:
            self.view.display_client(client)
            if client.get_commercial_id() == user_id:
                session.delete(client)
                session.commit()
                capture_message(f"Suppression client:{client.id}", level="info")
                self.view.display_info_message("Client supprimé avec succès.")
            else:
                self.view.display_warning_message(
                    "Ce client ne fait pas partie de votre équipe"
                )
        else:
            self.view.display_warning_message("Client non trouvé.")

    def read_all_client(self):
        try:
            clients = self.model.filter_all_clients()
            if clients:
                for client in clients:
                    self.view.display_client(client)
            else:
                self.view.display_info_message("Aucun client trouvé.")
        except Exception as e:
            self.view.display_error_message(
                f"Une erreur s'est produite lors de la récupération des clients : {e}"
            )

    def filter_client(self, user_role, user_id):
        if user_role == "commercial":
            self.view.filter_message("Voici la liste de vos clients:")
            try:
                clients = self.model.filter_by_commercial_id(user_id)
                if clients:
                    for client in clients:
                        self.view.display_client(client)
                else:
                    self.view.display_info_message("Aucun client trouvé.")
            except Exception as e:
                self.view.display_error_message(
                    f"Une erreur s'est produite lors de la récupération des clients : {e}"
                )
        else:
            self.view.display_info_message("Aucun filtre client disponible")

    def update_client(self, user_id):
        client_id = self.view.input_id_client()
        client = self.model.filter_by_id(client_id)
        if client:
            self.view.display_client(client)
            if client.get_commercial_id() == user_id:
                choice = self.view.ask_client_update_field()

                if choice == "nom":
                    new_name = self.view.input_name()
                    client.set_name(new_name)
                    client.set_last_update_date()
                    session.commit()
                    capture_message(
                        f"Modification nom client:{client.id}", level="info"
                    )
                    self.view.display_info_message("Nom du client modifié avec succès.")

                elif choice == "prenom":
                    new_surname = self.view.input_surname()
                    client.set_surname(new_surname)
                    client.set_last_update_date()
                    session.commit()
                    capture_message(
                        f"Modification prenom client:{client.id}", level="info"
                    )
                    self.view.display_info_message(
                        "Prénom du client modifié avec succès."
                    )

                elif choice == "email":
                    new_email = self.view.input_email()
                    client.set_email(new_email)
                    client.set_last_update_date()
                    session.commit()
                    capture_message(
                        f"Modification email client:{client.id}", level="info"
                    )
                    self.view.display_info_message(
                        "Email du client modifié avec succès."
                    )

                elif choice == "telephone":
                    new_phone = self.view.input_phone()
                    client.set_phone(new_phone)
                    client.set_last_update_date()
                    session.commit()
                    capture_message(
                        f"Modification telephone client:{client.id}", level="info"
                    )
                    self.view.display_info_message(
                        "Téléphone du client modifié avec succès."
                    )

                elif choice == "entreprise":
                    new_company = self.view.input_company()
                    client.set_company(new_company)
                    client.set_last_update_date()
                    session.commit()
                    capture_message(
                        f"Modification entreprise client:{client.id}", level="info"
                    )
                    self.view.display_info_message(
                        "Entreprise du client modifié avec succès."
                    )

                elif choice == "commercial":
                    new_commercial_id = self.view.input_id_commercial()
                    new_commercial = User.filter_by_id(new_commercial_id)
                    if (
                        new_commercial
                        and new_commercial.get_departement() == "commercial"
                    ):
                        client.set_commercial_id(new_commercial_id)
                        client.set_last_update_date()
                        session.commit()
                        capture_message(
                            f"Modification commercial client:{client.id}", level="info"
                        )
                        self.view.display_info_message(
                            "Commercial du client modifié avec succès."
                        )
                    else:
                        self.view.display_warning_message(
                            "L'ID spécifié n'appartient pas à un commercial."
                        )
                else:
                    self.view.display_warning_message("Option invalide.")
            else:
                self.view.display_warning_message(
                    "Ce client ne fait pas partie de votre équipe"
                )
        else:
            self.view.display_warning_message("Aucun client trouvé avec cet ID")
