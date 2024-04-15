from models.clients import Client




class ClientController:
    def __init__(self,session):

        self.session = session

    def inscrire_client(self, nom_complet, email, telephone, entreprise):
        nouveau_client = Client(nom_complet=nom_complet, email=email, telephone=telephone, entreprise=entreprise)
        self.session.add(nouveau_client)
        self.session.commit()
        print("Inscription réussie !")


    def connecter_client(self, email):
        client = self.session.query(Client).filter_by(email=email).first()
        if client:
            print("Connexion réussie !")
            return client
        else:
            print("Adresse e-mail non trouvée. Veuillez vous inscrire.")
            return None
