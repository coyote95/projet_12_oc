from models import User
import bcrypt


def test_role_from_departement(init_session):
    session = init_session
    user = User("lucas", "luccas@test.com", "commercial", "password")
    session.add(user)
    session.commit()
    assert user.role_id == 1


def test_filter_by_id(init_session):
    session = init_session
    user = User("lucas", "lucas@test.ctom", "commercial", "password")
    session.add(user)
    session.commit()
    find_user = user.filter_by_id(user.id)
    assert find_user.get_name() == "lucas"


def test_set_password(init_session):
    session = init_session
    user = User("lucas", "lucas@test.com", "commercial", None)
    password = "password"
    user.set_password(password)
    assert user.get_password() is not None
    assert bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
