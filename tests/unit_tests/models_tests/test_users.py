from models import User
from ...conftest import db_session, apply_patches
import bcrypt


@apply_patches
def test_role_from_departement(db_session):
    user = User("lucas", "luccas@test.com", "commercial", "password")
    db_session.add(user)
    db_session.commit()
    assert user.role_id == 1


@apply_patches
def test_filter_by_id(db_session):
    user = User("lucas", "lucas@test.com", "commercial", "password")
    db_session.add(user)
    db_session.commit()
    find_user = user.filter_by_id(user.id)
    assert find_user.name == "lucas"


def test_set_password():
    user = User("lucas", "lucas@test.com", "commercial", None)
    password = "password"
    user.set_password(password)
    assert user.password is not None
    assert bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
