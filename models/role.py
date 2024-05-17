from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import relationship
from . import Base


class Role(Base):
    """
    Represents a role entity in the database.

    Attributes:
        id (int): The unique identifier for the role.
        role (Enum): The role name, which can be one of 'commercial', 'support', or 'gestion'.
        users (relationship): Relationship with the User model representing users associated with the role.

    Methods:
        __init__(role): Initializes a new Role object with the provided role name.
        __str__(): Returns a string representation of the Role object.
        __repr__(): Returns a string representation of the Role object.
        has_permissions(): Returns a set of permissions associated with the role.
    """

    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    role = Column(Enum("commercial", "support", "gestion"), unique=True)
    users = relationship("User", passive_deletes="all")

    def __init__(self, role):
        self.role = role

    def __str__(self):
        return f"<Role(nom='{self.role}')>"

    def __repr__(self):
        return f"<Role(nom='{self.role}')>"

    def has_permissions(self):
        if self.role == "commercial":
            return {
                "read_user",
                "filter_user",
                "read_client",
                "filter_client",
                "create_client",
                "delete_client",
                "update_client",
                "read_contract",
                "filter_contract",
                "create_contract",
                "delete_contract",
                "update_contract",
                "read_event",
                "filter_event",
                "create_event",
                "delete_event",
                "update_event",
            }
        elif self.role == "gestion":
            return {
                "read_user",
                "filter_user",
                "create_user",
                "delete_user",
                "update_user",
                "read_client",
                "filter_client",
                "read_contract",
                "filter_contract",
                "create_contract",
                "delete_contract",
                "update_contract",
                "read_event",
                "filter_event",
                "update_event",
            }
        elif self.role == "support":
            return {
                "read_user",
                "filter_user",
                "read_client",
                "filter_client",
                "read_contract",
                "filter_contract",
                "read_event",
                "filter_event",
                "update_event",
            }
        else:
            return set()
