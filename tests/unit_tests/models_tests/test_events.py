from models import Event
from datetime import datetime


def test_filter_by_id(init_session):
    session = init_session
    event = Event(
        start_date=datetime(2024, 5, 15),
        end_date=datetime(2024, 5, 16),
        location="Conference Room",
        participants=50,
        notes="Example event",
    )
    session.add(event)
    session.commit()
    find_event = Event.filter_by_id(event.id)
    assert find_event.get_participants() == 50
