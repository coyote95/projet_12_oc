from models import Contract,User
from ...conftest import all_instances


# @apply_patches
# def test_filter_by_id(db_session):
#     find_contract = Contract.filter_by_id(1)
#     assert find_contract.S == "lucas"

def test_filter_by_id(all_instances, db_session):
    user, client, contract, event = all_instances

    # Utiliser les objets dans le test
    assert user.name == "Marc"
    assert client.name == "Alice"
    assert contract.total_price == 1000.0
    assert event.location == "Conference Room"

    # Vous pouvez également utiliser db_session pour effectuer d'autres opérations si nécessaire
    # Par exemple :
    db_session.query(User).filter_by(name="Marc").first()
