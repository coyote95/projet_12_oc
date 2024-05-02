from views.clients_view import ClientView
from models.clients import Client, ClientField
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
        print("Inscription réussie !")
        return new_client

    def delete_client_by_id(self, user_id):
        client_id = self.view.input_id_client()
        client = self.model.filter_by_id(client_id)
        if client:
            self.view.display_client(client)
            if client.get_commercial_id() == user_id:
                session.delete(client)
                session.commit()
                print("Utilisateur supprimé avec succès.")
            else:
                print("Ce client ne fait pas partie de votre équipe")
        else:
            print("Utilisateur non trouvé.")

    def read_all_client(self):
        try:
            clients = self.model.filter_all_clients()
            if clients:
                for client in clients:
                    self.view.display_client(client)
            else:
                print("Aucun client trouvé.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération des clients : {e}")

    def update_client(self, user_id):
        client_id = self.view.input_id_client()
        client = self.model.filter_by_id(client_id)
        if client:
            self.view.display_client(client)
            if client.get_user_id() == user_id:
                field = self.view.ask_client_update_field()

                if field == ClientField.NOM:
                    new_name = self.view.input_name()
                    client.set_name(new_name)
                    client.set_last_update_date()
                    session.commit()
                    print("Nom du client modifié avec succès.")

                elif field == ClientField.SURNAME:
                    new_surname = self.view.input_surname()
                    client.set_surname(new_surname)
                    client.set_last_update_date()
                    session.commit()
                    print("Prénom du client modifié avec succès.")

                elif field == ClientField.EMAIL:
                    new_email = self.view.input_email()
                    client.set_email(new_email)
                    client.set_last_update_date()
                    session.commit()
                    print("Email du client modifié avec succès.")

                elif field == ClientField.PHONE:
                    new_phone = self.view.input_phone()
                    client.set_phone(new_phone)
                    client.set_last_update_date()
                    session.commit()
                    print("Téléphone du client modifié avec succès.")

                elif field == ClientField.COMPANY:
                    new_company = self.view.input_company()
                    client.set_company(new_company)
                    client.set_last_update_date()
                    session.commit()
                    print("Entreprise du client modifié avec succès.")

                else:
                    print("Option invalide.")
            else:
                print("Ce client ne fait pas partie de votre équipe")
