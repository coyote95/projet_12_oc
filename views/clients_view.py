class ClientView:

    @staticmethod
    def afficher_message( message):
        print(message)

    @staticmethod
    def demander_infos_client():
        nom_complet = input("Entrez votre nom complet : ")
        email = input("Entrez votre adresse e-mail : ")
        telephone = input("Entrez votre numéro de téléphone : ")
        entreprise = input("Entrez le nom de votre entreprise : ")
        return nom_complet, email, telephone, entreprise
