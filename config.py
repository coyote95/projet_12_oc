from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:DATAstockage95?@localhost/epicevents', echo=True)

Session = sessionmaker(bind=engine)
session = Session()
