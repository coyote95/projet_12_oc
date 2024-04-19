from controllers.menu_controllers import ApplicationController
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base


from models.clients import Client
from models.users import User

from models.contract import Base as BaseContracts
from models.events import Base as BaseEvents


engine = create_engine('mysql+pymysql://root:DATAstockage95?@localhost/epicevents', echo=True)

# BaseUsers.metadata.create_all(engine)
Base.metadata.create_all(engine)
# BaseContracts.metadata.create_all(engine)
# BaseEvents.metadata.create_all(engine)

# Inspecter le schéma de la base de données pour voir les tables créées
inspector = inspect(engine)
tables = inspector.get_table_names()
print("Tables créées :", tables)

Session = sessionmaker(bind=engine)
session = Session()
app = ApplicationController(session, engine)
app.start()
