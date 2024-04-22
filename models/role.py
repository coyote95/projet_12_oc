from sqlalchemy import Column, String, Integer, Table, ForeignKey
from . import Base

# Modèle pour la table intermédiaire entre User et Role
user_role_association = Table('user_role_association', Base.metadata,
                              Column('user_id', Integer, ForeignKey('user.id')),
                              Column('role_id', Integer, ForeignKey('role.id'))
                              )


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
