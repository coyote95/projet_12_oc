from models.clients import Client
from views.contract_view import ContractView
from config import session


class ClientController:
    def __init__(self, contract):
        self.model = contract
        self.view = ContractView

    def add_contract(self, user_id):
        client_id = self.view.input_id_client()
        find_user_id = session.query(Client).filter_by(id=client_id).first()
        if find_user_id:
            if find_user_id == user_id:
                total_price, remaining_price = self.view.input_info_contract()
                new_contract = self.model(total_price=total_price, remaining_price=remaining_price,
                                          client_id=client_id)

                session.add(new_contract)
                session.commit()
                print("Contrat enregistée !")
                return new_contract
            else:
                print("Ce client ne fait pas partie de votre équipe")

        else:
            print("Client non trouvé pour l'ID donné.")


