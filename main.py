from controllers.menu_controllers import ApplicationController
from models import Base
from config import engine,session
from controllers.role_controllers import RoleController


Base.metadata.create_all(engine)

role_controller=RoleController()
role_controller.init_role_database()



# init_roles=['commercial','support','gestion']
# #controleur iniialisation base roles add
# for role in init_roles:
#     existing_role = session.query(Role).filter_by(role=role).first()
#     if existing_role is None:
#         # Créez une instance de la classe Role avec le nom du rôle
#         new_role = Role(role)
#         print(new_role)
#         # Ajoutez le rôle à la session
#         session.add(new_role)
#     else:
#         print(f"Le rôle '{role}' existe déjà dans la base de données.")
#
#     session.commit()



app = ApplicationController()
app.start()
