from controllers.menu_controllers import ApplicationController
from models import Base
from settings.database import engine
from controllers.role_controllers import RoleController
from settings import sentry

import sys


try:
    Base.metadata.create_all(engine)
except Exception as e:
    print("Erreur lors de la connexion à la base de données MySQL:", e)
    sys.exit(1)

try:
    role_controller = RoleController()
    role_controller.init_role_database()
except Exception as e:
    print(
        "Une erreur s'est produite lors de l'initialisation de la base de données des rôles:",
        e,
    )
    sys.exit(1)

app = ApplicationController()
app.start()
