from controllers.menu_controllers import ApplicationController
from models import Base
from settings.database import engine,session
from sqlalchemy.exc import OperationalError
from controllers.role_controllers import RoleController
import sentry_sdk
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
import sys

sentry_sdk.init(
    dsn="https://a7122892fad60f7545036ec00dda215e@o4507205449023488.ingest.de.sentry.io/4507205471633488",
    enable_tracing=True,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    integrations=[SqlalchemyIntegration()]

)


try:
    # Tenter de créer toutes les tables dans la base de données
    Base.metadata.create_all(engine)
except Exception as e:
    # Si une erreur de connexion MySQL se produit
    print("Erreur lors de la connexion à la base de données MySQL:", e)
    sys.exit(1)

try:
    role_controller = RoleController()
    role_controller.init_role_database()
except Exception as e:
    print("Une erreur s'est produite lors de l'initialisation de la base de données des rôles:", e)
    # Vous pouvez ajouter ici des opérations de gestion des erreurs, comme l'enregistrement dans un fichier journal, l'envoi d'un e-mail, etc.
    sys.exit(1)


app = ApplicationController()
app.start()
