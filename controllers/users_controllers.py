from views.users_view import UserView
from config import session


class UserController:
    def __init__(self, user):
        self.model = user
        self.view = UserView()

    def add_user(self):
        name, email, departement, password = self.view.input_infos_user()
        new_user = self.model(name=name, email=email, password=password, departement=departement)
        session.add(new_user)
        session.commit()
        print("Inscription réussie !")
        return new_user

    def connecter_user(self):
        name, password = self.view.ask_infos_user_login()
        return name, password


