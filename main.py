from controllers.menu_controllers import ApplicationController
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from models.clients import Base as BaseClients
from models.users import Base as BaseUsers


engine = create_engine('sqlite:///database.sql', echo=True)
BaseClients.metadata.create_all(engine)
BaseUsers.metadata.create_all(engine)

# Inspecter le schéma de la base de données pour voir les tables créées
inspector = inspect(engine)
tables = inspector.get_table_names()
print("Tables créées :", tables)

Session = sessionmaker(bind=engine)
session = Session()
app = ApplicationController(session, engine)
app.start()
