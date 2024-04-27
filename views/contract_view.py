
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
                remaining_price = float(input("Entrez le montant total du contrat: "))
                return remaining_price
            except ValueError:
                print("Vous n'avez pas saisi un nombre valide")

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
    def input_info_contract():
        total_price = ContractView.input_total_price()
        remaining_price = ContractView.input_remaining_price()
        return total_price,remaining_price