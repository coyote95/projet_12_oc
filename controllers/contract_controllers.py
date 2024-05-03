from models.clients import Client
from models.contract import Contract, ContractField
from views.contract_view import ContractView
from settings.database import session


class ContractController:
    def __init__(self):
        self.model = Contract
        self.view = ContractView()

    def create_contract(self, user_role, user_id):
        client_id = self.view.input_id_client()
        client = Client.filter_by_id(client_id)
        if client:
            if client.get_commercial_id() == user_id or user_role == 'gestion':
                total_price = self.view.input_total_price()
                while True:
                    remaining_price = self.view.input_remaining_price()
                    if remaining_price < total_price:
                        break
                    else:
                        self.view.display_error_message("le prix restant à payer doit être inférieur au prix total")

                signed = self.view.input_signed_contract()
                new_contract = self.model(total_price=total_price, remaining_price=remaining_price,
                                          client_id=client_id, signed=signed)

                session.add(new_contract)
                session.commit()
                self.view.display_info_message("Contrat enregistée !")
                return new_contract
            else:
                self.view.display_warning_message("Ce client ne fait pas partie de votre équipe")

        else:
            self.view.display_warning_message("Client non trouvé pour l'ID donné.")

    def delete_contract_by_id(self, user_role, user_id):
        contract_id = self.view.input_id_contract()
        contract = Contract.filter_by_id(contract_id)
        if contract:
            self.view.display_contract(contract)
            if contract.client.get_commercial_id() == user_id or user_role == 'gestion':
                session.delete(contract)
                session.commit()
                self.view.display_info_message("Contrat supprimé avec succès.")
            else:
                self.view.display_warning_message("Ce contrat de client ne fait pas partie de votre équipe")

        else:
            self.view.display_warning_message("contrat non trouvé.")

    def read_all_contracts(self):
        try:
            contracts = Contract.filter_all_contracts()
            if contracts:
                for contract in contracts:
                    self.view.display_contract(contract)
            else:
                self.view.display_warning_message("Aucun contrat trouvé.")
        except Exception as e:
            self.view.display_warning_message(f"Une erreur s'est produite lors de la récupération des contrats : {e}")

    def update_contract(self, user_role, user_id):
        contract_id = self.view.input_id_contract()
        contract = Contract.filter_by_id(contract_id)
        if contract:
            self.view.display_contract(contract)
            if contract.client.get_commercial_id() == user_id or user_role == 'gestion':
                field = self.view.ask_contract_update_field()

                if field == ContractField.TOTAL_PRICE:
                    new_total_price = self.view.input_total_price()
                    contract.set_total_price(new_total_price)
                    session.commit()
                    self.view.display_info_message("Prix total modifié avec succès.")

                elif field == ContractField.REMAINING_PRICE:
                    new_remaining_price = self.view.input_remaining_price()
                    contract.set_remaining_price(new_remaining_price)
                    session.commit()
                    self.view.display_info_message("Prix restant modifié avec succès.")

                elif field == ContractField.SIGNED:
                    new_signed_contract = self.view.input_signed_contract()
                    contract.set_signed(new_signed_contract)
                    session.commit()
                    self.view.display_info_message("Statut signature modifié avec succès.")

                elif field == ContractField.CLIENT_ID:
                    new_client_id = self.view.input_id_client()
                    contract.set_client_id(new_client_id)
                    session.commit()
                    self.view.display_info_message("Client du contrat modifié avec succès.")

                # elif field == ContractField.EVENT:
                #     new_event = self.view.inpu
                #     client.comapgny = new_company
                #     client.set_last_update_date()
                #     session.commit()
                #     print("Entreprise du client modifié avec succès.")

                else:
                    self.view.display_warning_message("Option invalide.")
            else:
                self.view.display_warning_message("Ce client ne fait pas partie de votre équipe")

