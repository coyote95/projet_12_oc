from models import User
from ...conftest import  patched_session
import bcrypt


def test_role_from_departement(patched_session):
    user = User("lucas", "luccas@test.com", "commercial", "password")
    patched_session.add(user)
    patched_session.commit()
    assert user.role_id == 1


def test_filter_by_id(patched_session):
    user = User("lucas", "lucas@test.com", "commercial", "password")
    patched_session.add(user)
    patched_session.commit()
    find_user = user.filter_by_id(user.id)
    assert find_user.get_name()== "lucas"


def test_set_password():
    user = User("lucas", "lucas@test.com", "commercial", None)
    password = "password"
    user.set_password(password)
    assert user.get_password() is not None
    assert bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
