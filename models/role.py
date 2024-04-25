from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from . import Base


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    role = Column(String(255))
    users = relationship('User', back_populates='role', passive_deletes='all')

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
