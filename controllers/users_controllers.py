from views.users_view import UserView


class UserController:
    def __init__(self, user):
        self.model = user
        self.view = UserView()

    def inscription_user(self):
        print("Inscription réussie !")
        name, email, departement, password = self.view.input_infos_user()
        return self.model(name=name, email=email, password=password, departement=departement)

    # def connecter_client(self, email):
    #     client = self.session.query(Client).filter_by(email=email).first()
    #     if client:
    #         print("Connexion réussie !")
    #         return client
    #     else:
    #         print("Adresse e-mail non trouvée. Veuillez vous inscrire.")
    #         return None
