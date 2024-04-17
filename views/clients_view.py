class ClientView:

    @staticmethod
    def afficher_message(message):
        print(message)

    @staticmethod
    def add_client():
        name = input("Entrez votre nom complet : ")
        email = input("Entrez votre adresse e-mail : ")
        phone = input("Entrez votre numéro de téléphone : ")
        company = input("Entrez le nom de votre entreprise : ")
        return name, email, phone, company
