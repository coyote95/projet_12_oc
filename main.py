from controllers.menu_controllers import ApplicationController
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base
import os

# # Chemin du répertoire de l'application
# app_dir = os.path.dirname(os.path.abspath(__file__))
#
# # Chemin du fichier config.ini dans le répertoire de l'application
# config_file = os.path.join(app_dir, 'config.ini')


engine = create_engine('mysql+pymysql://root:DATAstockage95?@localhost/epicevents', echo=True)

Base.metadata.create_all(engine)

# Inspecter le schéma de la base de données pour voir les tables créées
inspector = inspect(engine)
tables = inspector.get_table_names()
print("Tables créées :", tables)

Session = sessionmaker(bind=engine)
session = Session()
app = ApplicationController(session, engine)
app.start()
