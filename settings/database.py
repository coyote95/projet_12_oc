from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

if "PYTEST_VERSION" in os.environ:
    database = "sqlite:///:memory:"
else:
    from settings.setting import database

engine = create_engine(database, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

