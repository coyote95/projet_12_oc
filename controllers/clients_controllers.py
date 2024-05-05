from views.clients_view import ClientView
from models.clients import Client
from models.users import User
from settings.database import session


class ClientController:
    def __init__(self):
        self.model = Client
        self.view = ClientView()

    def create_client(self, user_id):
        name, surname, email, phone, company = self.view.input_info_client()
        new_client = self.model(name=name, surname=surname, email=email, phone=phone, company=company)
        new_client.set_commercial_id(user_id)
        session.add(new_client)
        session.commit()
        self.view.display_info_message("Inscription réussie !")
        return new_client

    def delete_client_by_id(self, user_id):
        client_id = self.view.input_id_client()
        client = self.model.filter_by_id(client_id)
        if client:
            self.view.display_client(client)
            if client.get_commercial_id() == user_id:
                session.delete(client)
                session.commit()
                self.view.display_info_message("Utilisateur supprimé avec succès.")
            else:
                self.view.display_warning_message("Ce client ne fait pas partie de votre équipe")
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
            self.view.display_error_message(f"Une erreur s'est produite lors de la récupération des clients : {e}")

    def filter_client(self, user_role, user_id):
        if user_role == 'commercial':
            self.view.filter_message("Voici la liste de vos clients:")
            try:
                clients = self.model.filter_by_commercial_id(user_id)
                if clients:
                    for client in clients:
                        self.view.display_client(client)
                else:
                    self.view.display_info_message("Aucun client trouvé.")
            except Exception as e:
                self.view.display_error_message(f"Une erreur s'est produite lors de la récupération des clients : {e}")
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
                    self.view.display_info_message("Nom du client modifié avec succès.")

                elif choice == "prenom":
                    new_surname = self.view.input_surname()
                    client.set_surname(new_surname)
                    client.set_last_update_date()
                    session.commit()
                    self.view.display_info_message("Prénom du client modifié avec succès.")

                elif choice == "email":
                    new_email = self.view.input_email()
                    client.set_email(new_email)
                    client.set_last_update_date()
                    session.commit()
                    self.view.display_info_message("Email du client modifié avec succès.")

                elif choice == "telephone":
                    new_phone = self.view.input_phone()
                    client.set_phone(new_phone)
                    client.set_last_update_date()
                    session.commit()
                    self.view.display_info_message("Téléphone du client modifié avec succès.")

                elif choice == "entreprise":
                    new_company = self.view.input_company()
                    client.set_company(new_company)
                    client.set_last_update_date()
                    session.commit()
                    self.view.display_info_message("Entreprise du client modifié avec succès.")

                elif choice == "commercial":
                    new_commercial_id = self.view.input_id_commercial()
                    new_commercial=User.filter_by_id(new_commercial_id)
                    if new_commercial and new_commercial.get_departement() == 'commercial':
                        client.set_commercial_id(new_commercial_id)
                        client.set_last_update_date()
                        session.commit()
                        self.view.display_info_message("Entreprise du client modifié avec succès.")
                    else:
                        self.view.display_warning_message("L'ID spécifié n'appartient pas à un commercial.")
                else:
                    self.view.display_warning_message("Option invalide.")
            else:
                self.view.display_warning_message("Ce client ne fait pas partie de votre équipe")
        else:
            self.view.display_warning_message("Aucun client trouvé avec cet ID")
