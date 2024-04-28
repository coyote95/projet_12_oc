from models.clients import Client
from models.contract import Contract
from views.contract_view import ContractView
from config import session


class ContractController:
    def __init__(self, contract):
        self.model = contract
        self.view = ContractView

    def add_contract(self, user_role, user_id):
        client_id = self.view.input_id_client()
        find_client = session.query(Client).filter_by(id=client_id).first()
        if find_client:
            if find_client.user_id == user_id or user_role == 'gestion':
                total_price, remaining_price, contract_signed = self.view.input_info_contract()
                new_contract = self.model(total_price=total_price, remaining_price=remaining_price,
                                          client_id=client_id, signed_contract=contract_signed)

                session.add(new_contract)
                session.commit()
                print("Contrat enregistée !")
                return new_contract
            else:
                print("Ce client ne fait pas partie de votre équipe")

        else:
            print("Client non trouvé pour l'ID donné.")

    def delete_contract_by_id(self, user_role, user_id):
        contract_id = self.view.input_id_contract()
        contract = session.query(Contract).filter_by(id=contract_id).first()

        if contract:
            if contract.client.user_id == user_id or user_role == 'gestion':
                session.delete(contract)
                session.commit()
                print("Contrat supprimé avec succès.")
            else:
                print("Ce contrat de client ne fait pas partie de votre équipe")
        else:
            print("contrat non trouvé.")

    def read_all_contracts(self):
        try:
            contracts = session.query(self.model).all()
            if contracts:
                for contract in contracts:
                    self.view.display_contract(contract)
            else:
                print("Aucun contrat trouvé.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération des contrats : {e}")
