from models.clients import Client
from models.contract import Contract, ContractField
from views.contract_view import ContractView
from settings.database import session


class ContractController:
    def __init__(self):
        self.model = Contract
        self.view = ContractView()

    def add_contract(self, user_role, user_id):
        client_id = self.view.input_id_client()
        client = session.query(Client).filter_by(id=client_id).first()
        if client:
            if client.get_commercial_id() == user_id or user_role == 'gestion':
                total_price, remaining_price, signed = self.view.input_info_contract()
                new_contract = self.model(total_price=total_price, remaining_price=remaining_price,
                                          client_id=client_id, signed=signed)

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
            self.view.display_contract(contract)
            if contract.client.get_commercial_id() == user_id or user_role == 'gestion':
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

    def update_contract(self, user_role, user_id):
        contract_id = self.view.input_id_contract()
        contract = session.query(self.model).filter_by(id=contract_id).first()
        if contract:
            self.view.display_contract(contract)
            if contract.client.get_commercial_id()== user_id or user_role == 'gestion':
                field = self.view.ask_contract_update_field()

                if field == ContractField.TOTAL_PRICE:
                    new_total_price = self.view.input_total_price()
                    contract.set_total_price(new_total_price)
                    session.commit()
                    print("Prix total modifié avec succès.")

                elif field == ContractField.REMAINING_PRICE:
                    new_remaining_price = self.view.input_remaining_price()
                    contract.set_remaining_price(new_remaining_price)
                    session.commit()
                    print("Prix restant modifié avec succès.")

                elif field == ContractField.SIGNED:
                    new_signed_contract = self.view.input_signed_contract()
                    contract.set_signed(new_signed_contract)
                    session.commit()
                    print("Statut signature modifié avec succès.")

                elif field == ContractField.CLIENT_ID:
                    new_client_id = self.view.input_id_client()
                    contract.set_client_id(new_client_id)
                    session.commit()
                    print("Client du contrat modifié avec succès.")

                # elif field == ContractField.EVENT:
                #     new_event = self.view.inpu
                #     client.comapgny = new_company
                #     client.set_last_update_date()
                #     session.commit()
                #     print("Entreprise du client modifié avec succès.")

                else:
                    print("Option invalide.")
            else:
                print("Ce client ne fait pas partie de votre équipe")