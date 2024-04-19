from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    departement = Column(Enum('commercial', 'support', 'gestion'))
    password = Column(String(255))
    clients = relationship('Client', backref="users")


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    email = Column(String(255), unique=True)
    phone = Column(Integer)
    company = Column(String(255))
    creation_date = Column(DateTime)
    last_update = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')


engine = create_engine('mysql+pymysql://root:DATAstockage95?@localhost/tests', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



