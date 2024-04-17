from models.clients import Client
from views.clients_view import ClientView


class ClientController:
    def __init__(self, client):
        self.model = client
        self.view = ClientView

    def add_client(self):
        name, email, phone, company = self.view.add_client()
        new_client = self.model(name=name, email=email, phone=phone, company=company)
        print("Inscription réussie !")
        return new_client
