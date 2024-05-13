from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import relationship
from . import Base


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    role = Column(Enum('commercial', 'support', 'gestion'), unique=True)
    users = relationship('User', passive_deletes='all')

    def __init__(self, role):
        self.role = role

    def __str__(self):
        return f"<Role(nom='{self.role}')>"

    def __repr__(self):
        return f"<Role(nom='{self.role}')>"
    #
    # def has_user_permissions(self):
    #     if self.role == "commercial":
    #         return ["read_user", "filter_user"]
    #     elif self.role == "gestion":
    #         return ["read_user", "filter_user", "create_user", "delete_user", "update_user"]
    #     elif self.role == "support":
    #         return ["read_user", "filter_user"]
    #     else:
    #         return []
    #
    # def has_client_permissions(self):
    #     if self.role == "commercial":
    #         return ["read_client", "filter_client", "create_client", "delete_client", "update_client"]
    #     elif self.role == "gestion":
    #         return ["read_client", "filter_client"]
    #     elif self.role == "support":
    #         return ["read_client", "filter_client"]
    #     else:
    #         return []
    #
    # def has_contract_permissions(self):
    #     if self.role == "commercial":
    #         return ["read_contract", "filter_contract", "create_contract", "delete_contract", "update_contract"]
    #     elif self.role == "gestion":
    #         return ["read_contract", "filter_contract", "create_contract", "delete_contract", "update_contract"]
    #     elif self.role == "support":
    #         return ["read_contract", "filter_contract"]
    #     else:
    #         return []
    #
    # def has_event_permissions(self):
    #     if self.role == "commercial":
    #         return ["read_event", "filter_event", "create_event", "delete_event", "update_event"]
    #     elif self.role == "gestion":
    #         return ["read_event", "filter_event", "update_event"]
    #     elif self.role == "support":
    #         return ["read_event", "filter_event", "update_event"]
    #     else:
    #         return []

    def has_permissions(self):
        if self.role == "commercial":
            return {"read_user", "filter_user",
                    "read_client", "filter_client", "create_client", "delete_client", "update_client",
                    "read_contract", "filter_contract", "create_contract", "delete_contract", "update_contract",
                    "read_event", "filter_event", "create_event", "delete_event", "update_event"}
        elif self.role == "gestion":
            return {"read_user", "filter_user", "create_user", "delete_user", "update_user",
                    "read_client", "filter_client",
                    "read_contract", "filter_contract", "create_contract", "delete_contract", "update_contract",
                    "read_event", "filter_event", "update_event"}
        elif self.role == "support":
            return {"read_user", "filter_user",
                    "read_client", "filter_client",
                    "read_contract", "filter_contract",
                    "read_event", "filter_event", "update_event"}
        else:
            return set()
