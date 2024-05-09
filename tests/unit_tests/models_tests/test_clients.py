from models import Client
from ...conftest import db_session


def test_filter_by_id(patched_session):
    client = Client("mola", "jessica", "jessica@test.com", "0123654789", "sncf")
    patched_session.add(client)
    patched_session.commit()
    find_client = client.filter_by_id(client.id)
    assert find_client.surname == "jessica"
