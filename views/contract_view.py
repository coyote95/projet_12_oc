from views.base_view import BaseView


class ContractView(BaseView):
    """
    Provides methods for user input and displaying contract information.

    Inherits from:
        BaseView: A base class providing methods to display messages in different colors.

    Methods:
        input_total_price(): Prompts the user to input the total price of the contract.
        input_remaining_price(): Prompts the user to input the remaining price to pay.
        input_signed_contract(): Prompts the user to input whether the contract is signed or not.
        display_signed_contract(signed_contract): Displays the status of the contract's signature.
        input_id_client(): Prompts the user to input the client's ID associated with the contract.
        input_id_contract(): Prompts the user to input the contract's ID.
        input_prices(): Prompts the user to input both total and remaining prices.
        display_contract(contract): Displays information about a contract.
        ask_contract_update_field(): Asks the user which field of the contract they want to update.
        menu_filter(): Displays a menu for filtering contract options.
    """

    @staticmethod
    def input_total_price():
        while True:
            try:
                total_price = float(input("Entrez le montant total du contrat: "))
                return total_price
            except ValueError:
                ContractView.display_error_message("Vous n'avez pas saisi un numéro")

    @staticmethod
    def input_remaining_price():
        while True:
            try:
                remaining_price = float(input("Entrez la somme restante à payer: "))
                return remaining_price
            except ValueError:
                ContractView.display_error_message("Vous n'avez pas saisi un numéro")

    @staticmethod
    def input_signed_contract():
        while True:
            signed_contract = input("Le client a-t-il signé le contrat (oui/non): ")
            if signed_contract.lower() == "oui":
                return True
            elif signed_contract.lower() == "non":
                return False
            else:
                ContractView.display_error_message(
                    "Vous n'avez pas saisi 'oui' ou 'non'"
                )

    @staticmethod
    def display_signed_contract(signed_contract):
        if signed_contract == 1:
            return "oui"
        elif signed_contract == 0:
            return "non"

    @staticmethod
    def input_id_client():
        while True:
            client_id = input("Entrez l'id du client: ")
            try:
                client_id = int(client_id)
                return client_id
            except ValueError:
                ContractView.display_error_message("Vous n'avez pas saisi un numéro")

    @staticmethod
    def input_id_contract():
        while True:
            contract_id = input("Entrez l'id du contrat: ")
            try:
                contract_id = int(contract_id)
                return contract_id
            except ValueError:
                ContractView.display_error_message("Vous n'avez pas saisi un numéro")

    @staticmethod
    def input_prices():
        total_price = ContractView.input_total_price()
        remaining_price = ContractView.input_remaining_price()
        return total_price, remaining_price

    @staticmethod
    def display_contract(contract):
        print(
            f"id:{contract.get_id()}    "
            f"Client:{contract.get_client()}    "
            f"Prix total:{contract.get_total_price()}    "
            f"Prix restant à payer:{contract.get_remaining_price()}    "
            f"Contrat signé:{ContractView.display_signed_contract(contract.get_signed())}    "
        )

    @staticmethod
    def ask_contract_update_field():
        while True:
            try:
                choice = int(
                    input(
                        f"Quelle information voulez-vous modifier?\n"
                        f"1:Prix total \n"
                        f"2:Prix restant\n"
                        f"3:Statut signature\n"
                        f"4:Numéro de Client\n"
                    )
                )
                if choice == 1:
                    return "prix_total"
                elif choice == 2:
                    return "prix_restant"
                elif choice == 3:
                    return "signature"
                elif choice == 4:
                    return "client"
                else:
                    ContractView.display_warning_message(
                        "Vous n'avez pas saisi un numéro valide"
                    )

            except ValueError:
                ContractView.display_error_message("Vous n'avez pas saisi un numéro")

    @staticmethod
    def menu_filter():
        while True:
            try:
                choice = int(
                    input(
                        f"Quelle filtrage voulez-vous réaliser?\n"
                        f"1: Liste des contrats non signés\n"
                        f"2: Liste des contrats restants à payer\n"
                        f"Votre choix: "
                    )
                )
                if choice == 1:
                    print("Voici la liste des contrats non signés")
                    return 1
                elif choice == 2:
                    print("Voici la liste des contrats non payés")
                    return 2
                else:
                    ContractView.display_warning_message(
                        "Vous n'avez pas saisi un numéro valide"
                    )

            except ValueError:
                ContractView.display_error_message("Vous n'avez pas saisi un numéro")
