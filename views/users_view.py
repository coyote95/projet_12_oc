class UserView:

    @staticmethod
    def afficher_message( message):
        print(message)

    @staticmethod
    def input_infos_user():
        name = input("Entrez votre nom complet : ")
        email = input("Entrez votre adresse e-mail : ")
        departement= input("Entrez le departement: ")
        password = input("Entrez votre mot de passe : ")
        return name, email, departement, password
