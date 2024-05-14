from models import Client


def test_filter_by_id(init_session):
    session = init_session
    client = Client("mola", "jessica", "jessica@test.com", "0123654789", "sncf")
    session.add(client)
    session.commit()
    find_client = client.filter_by_id(client.id)
    assert find_client.get_surname() == "jessica"
