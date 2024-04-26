import re


class ClientView:

    @staticmethod
    def afficher_message(message):
        print(message)

    @staticmethod
    def input_name():
        name = input("Entrez votre nom: ")
        return name.upper()

    @staticmethod
    def input_surname():
        name = input("Entrez votre prénom: ")
        return name.upper()

    @staticmethod
    def input_company():
        name = input("Entrez votre entreprise: ")
        return name.lower()

    @staticmethod
    def input_phone():
        while True:
            try:
                phone = input("Entrez votre numéro de téléphone:")
                if len(phone) == 6 and phone.isdigit():
                    return int(phone)
                else:
                    print("Votre numéro ne comporte pas 6 chiffres")
            except ValueError:
                print("Vous n'avez pas saisi un entier")

    @staticmethod
    def input_email():
        while True:
            email = input("Entrez votre email: ")
            # Expression régulière pour valider le format de l'email
            if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                return email
            else:
                print("Adresse email invalide. Veuillez réessayer.")

    @staticmethod
    def input_info_client():
        name = ClientView.input_name()
        surname=ClientView.input_surname()
        email = ClientView.input_email()
        phone = ClientView.input_phone()
        company = ClientView.input_company()
        return name, surname, email,phone,company
