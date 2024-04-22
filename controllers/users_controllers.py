from views.users_view import UserView


class UserController:
    def __init__(self, user):
        self.model = user
        self.view = UserView()

    def inscription_user(self):
        name, email, departement, password = self.view.input_infos_user()
        new_user = self.model(name=name, email=email, password=password, departement=departement)
        print("Inscription réussie !")
        return new_user

    def connecter_user(self):
        name,password= self.view.ask_infos_user_login()
        return name, password

        # if name == self.model.name and password == self.model.check_password:
        #     print("Connexion réussie !")
        #     return self.model
        # else:
        #     print("Adresse e-mail non trouvée. Veuillez vous inscrire.")
        #     return None
