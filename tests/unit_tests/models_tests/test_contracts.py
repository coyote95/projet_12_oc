from models import Contract
from ...conftest import patched_session


def test_filter_by_id(patched_session):
    contract = Contract(total_price=1000.0, remaining_price=500.0, signed=True)
    patched_session.add(contract)
    patched_session.commit()
    find_contract = Contract.filter_by_id(contract.id)
    assert find_contract.get_total_price() == 1000.0


# def test_filter_by_id(session_all_instances):
#     user, client, contract, event, session = session_all_instances
#
#     # Utiliser les objets dans le test
#     assert user.name == "Marc"
#     assert client.name == "Alice"
#     assert contract.total_price == 1000.0
#     assert event.location == "Conference Room"
#
#     # Vous pouvez également utiliser db_session pour effectuer d'autres opérations si nécessaire
#     session.query(User).filter_by(name="Marc").first()
