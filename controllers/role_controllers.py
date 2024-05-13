from views.users_view import UserView
from models.role import Role
from settings.database import session


class RoleController:
    def __init__(self):
        self.model = Role
        self.view = UserView()

    def init_role_database(self):

        init_roles = ['commercial', 'support', 'gestion']
        # controleur iniialisation base roles add
        for role in init_roles:
            existing_role = session.query(self.model).filter_by(role=role).first()
            if existing_role is None:
                # Créez une instance de la classe Role avec le nom du rôle
                new_role = self.model(role)
                # Ajoutez le rôle à la session
                session.add(new_role)

            session.commit()
