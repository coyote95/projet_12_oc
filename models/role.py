from sqlalchemy import Column, String, Integer, Table, ForeignKey,Enum
from . import Base

# Modèle pour la table intermédiaire entre User et Role
user_role_association = Table('user_role_association', Base.metadata,
                              Column('user_id', Integer, ForeignKey('user.id')),
                              Column('role_id', Integer, ForeignKey('role.id'))
                              )


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    role = Column(String(255))

    def __init__(self, role):
        self.role = role

    def has_user_permissions(self):
        if self.role == "commercial":
            return ["read_user"]
        elif self.role == "gestion":
            return ["create_user", "delete_user", "update_user", "edit_user"]
        elif self.role == "support":
            return ["read_user"]
        else:
            return []
