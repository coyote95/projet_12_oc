from models.clients import Client
from views.clients_view import ClientView
from config import session


class ClientController:
    def __init__(self, client):
        self.model = client
        self.view = ClientView

    def add_client(self, user_id):
        name, surname, email, phone, company = self.view.input_info_client()
        new_client = self.model(name=name, surname=surname, email=email, phone=phone, company=company)
        new_client.user_id = user_id
        session.add(new_client)
        session.commit()
        print("Inscription réussie !")
        return new_client
