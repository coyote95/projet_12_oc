from controllers.menu_controllers import ApplicationController
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models.clients import Base

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

# Inspecter le schéma de la base de données pour voir les tables créées
inspector = inspect(engine)
tables = inspector.get_table_names()
print("Tables créées :", tables)

Session = sessionmaker(bind=engine)
session = Session()
app = ApplicationController(session,engine)
app.start()
