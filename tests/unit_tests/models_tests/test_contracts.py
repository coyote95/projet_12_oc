from models import Contract


def test_filter_by_id(init_session):
    session = init_session
    contract = Contract(total_price=1000.0, remaining_price=500.0, signed=True)
    session.add(contract)
    session.commit()
    find_contract = Contract.filter_by_id(contract.id)
    assert find_contract.get_total_price() == 1000.0
