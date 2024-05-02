from models.contract import ContractField


class ContractView:

    @staticmethod
    def afficher_message(message):
        print(message)

    @staticmethod
    def input_total_price():
        while True:
            try:
                total_price = float(input("Entrez le montant total du contrat: "))
                return total_price
            except ValueError:
                print("Vous n'avez pas saisi un nombre valide")

    @staticmethod
    def input_remaining_price():
        while True:
            try:
                remaining_price = float(input("Entrez la somme restante à payer: "))
                return remaining_price
            except ValueError:
                print("Vous n'avez pas saisi un nombre valide")

    @staticmethod
    def input_signed_contract():
        while True:
            try:
                signed_contract = input("Le client a-t-il signé le contrat (oui/non): ")
                if signed_contract.lower() == "oui":
                    return True
                elif signed_contract.lower() == "non":
                    return False
            except ValueError:
                print("Vous n'avez pas saisi 'oui' ou 'non'")

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
                print("Vous n'avez pas écrit un entier.")

    @staticmethod
    def input_id_contract():
        while True:
            contract_id = input("Entrez l'id du contrat: ")
            try:
                contract_id = int(contract_id)
                return contract_id
            except ValueError:
                print("Vous n'avez pas écrit un entier.")

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
                choice = int(input(
                    f"Quelle information voulez-vous modifier?\n"
                    f"1:total prix {ContractField.TOTAL_PRICE}\n"
                    f"2: {ContractField.REMAINING_PRICE.name}\n"
                    f"3: {ContractField.SIGNED.name}\n"
                    f"4: {ContractField.CLIENT_ID.name}\n"
                    f"5: {ContractField.EVENT.name}\n"
                ))
                field = ContractField(choice)
                if field in ContractField:
                    return field
                else:
                    print("Vous n'avez pas écrit un numéro valide.")
            except ValueError:
                print("Vous devez entrer un entier.")
