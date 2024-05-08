from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings.setting import database

engine = create_engine(database, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

numero=10

