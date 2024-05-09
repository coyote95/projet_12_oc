from models import Event
from ...conftest import patched_session
from datetime import datetime


def test_filter_by_id(patched_session):
    event = Event(
        start_date=datetime(2024, 5, 15),
        end_date=datetime(2024, 5, 16),
        location="Conference Room",
        participants=50,
        notes="Example event",
    )
    patched_session.add(event)
    patched_session.commit()
    find_event = Event.filter_by_id(event.id)
    assert find_event.get_participants() == 50
