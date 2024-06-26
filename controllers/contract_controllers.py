"""
ContractController module for managing contract-related operations.

Classes:
    ContractController: Manages contract operations and interactions with the database and view.

Methods:
    __init__(self):
        Initializes the ContractController with a Contract model and ContractView.

    create_contract(self, user_role, user_id):
        Creates a new contract with user input if the user is authorized.

    delete_contract_by_id(self, user_role, user_id):
        Deletes a contract by ID if the user is authorized.

    read_all_contracts(self):
        Retrieves and displays all contracts from the database.

    filter_contracts(self, user_role):
        Filters and displays contracts based on the user's role and selected filter.

    update_contract(self, user_role, user_id):
        Updates contract information based on user input if the user is authorized.
"""

from models import Client
from models import Contract
from views import ContractView
from settings.database import session
from sentry_sdk import capture_message


class ContractController:
    def __init__(self):
        self.model = Contract
        self.view = ContractView()

    def create_contract(self, user_role, user_id):
        client_id = self.view.input_id_client()
        client = Client.filter_by_id(client_id)
        if client:
            if client.get_commercial_id() == user_id or user_role == "gestion":
                total_price = self.view.input_total_price()
                while True:
                    remaining_price = self.view.input_remaining_price()
                    if remaining_price < total_price:
                        break
                    else:
                        self.view.display_error_message(
                            "le prix restant à payer doit être inférieur au prix total"
                        )
                signed = self.view.input_signed_contract()
                new_contract = self.model(
                    total_price=total_price,
                    remaining_price=remaining_price,
                    client_id=client_id,
                    signed=signed,
                )
                session.add(new_contract)
                session.commit()
                capture_message(f"Création contrat:{new_contract.id}", level="info")
                self.view.display_info_message("Contrat enregistée !")
                return new_contract
            else:
                self.view.display_warning_message(
                    "Ce client ne fait pas partie de votre équipe"
                )
        else:
            self.view.display_warning_message("Client non trouvé pour l'ID donné.")

    def delete_contract_by_id(self, user_role, user_id):
        contract_id = self.view.input_id_contract()
        contract = Contract.filter_by_id(contract_id)
        if contract:
            self.view.display_contract(contract)
            if contract.client.get_commercial_id() == user_id or user_role == "gestion":
                session.delete(contract)
                session.commit()
                capture_message(f"Suppression contrat:{contract.id}", level="info")
                self.view.display_info_message("Contrat supprimé avec succès.")
            else:
                self.view.display_warning_message(
                    "Ce contrat de client ne fait pas partie de votre équipe"
                )
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
            self.view.display_warning_message(
                f"Une erreur s'est produite lors de la récupération des contrats : {e}"
            )

    def filter_contracts(self, user_role):
        if user_role == "commercial":
            choice = self.view.menu_filter()
            if choice == 1:
                try:
                    contracts = self.model.filter_unsigned()
                    if contracts:
                        for contract in contracts:
                            self.view.display_contract(contract)
                    else:
                        self.view.display_info_message("Aucun contrat non signé.")
                except Exception as e:
                    self.view.display_error_message(
                        f"Une erreur s'est produite lors de la récupération des contrats: {e}"
                    )
            elif choice == 2:
                try:
                    contracts = self.model.filter_unpayed()
                    if contracts:
                        for contract in contracts:
                            self.view.display_contract(contract)
                    else:
                        self.view.display_info_message("Aucun contrat non payé.")
                except Exception as e:
                    self.view.display_error_message(
                        f"Une erreur s'est produite lors de la récupération des contrats: {e}"
                    )
        else:
            self.view.display_info_message("Aucun filtre contrat disponible")

    def update_contract(self, user_role, user_id):
        contract_id = self.view.input_id_contract()
        contract = Contract.filter_by_id(contract_id)
        if contract:
            self.view.display_contract(contract)
            if contract.client.get_commercial_id() == user_id or user_role == "gestion":
                choice = self.view.ask_contract_update_field()

                if choice == "prix_total":
                    new_total_price = self.view.input_total_price()
                    contract.set_total_price(new_total_price)
                    session.commit()
                    capture_message(
                        f"Modification prix total contrat:{contract.id}", level="info"
                    )
                    self.view.display_info_message("Prix total modifié avec succès.")

                elif choice == "prix_restant":
                    new_remaining_price = self.view.input_remaining_price()
                    contract.set_remaining_price(new_remaining_price)
                    session.commit()
                    capture_message(
                        f"Modification prix restant contrat:{contract.id}", level="info"
                    )
                    self.view.display_info_message("Prix restant modifié avec succès.")

                elif choice == "signature":
                    new_signed_contract = self.view.input_signed_contract()
                    contract.set_signed(new_signed_contract)
                    session.commit()
                    capture_message(
                        f"Modification signature contrat:{contract.id}", level="info"
                    )
                    self.view.display_info_message(
                        "Statut signature modifié avec succès."
                    )

                elif choice == "client":
                    new_client_id = self.view.input_id_client()
                    contract.set_client_id(new_client_id)
                    session.commit()
                    capture_message(
                        f"Modification client contrat:{contract.id}", level="info"
                    )
                    self.view.display_info_message(
                        "Client du contrat modifié avec succès."
                    )

                else:
                    self.view.display_warning_message("Option invalide.")
            else:
                self.view.display_warning_message(
                    "Ce client ne fait pas partie de votre équipe"
                )
        else:
            self.view.display_warning_message("Aucun contract trouvé avec cet ID")
