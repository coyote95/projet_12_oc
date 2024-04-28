from models.clients import Client
from models.events import Event
from models.contract import Contract
from views.event_view import EventView
from config import session


class EventController:
    def __init__(self):
        self.model = Event
        self.view = EventView

    def add_event(self, user_role, user_id):
        contract_id = self.view.input_id_contract()
        contrat = session.query(Contract).filter_by(id=contract_id).first()
        if contrat:
            if contrat.client.user_id == user_id or user_role == 'support':
                start_date, end_date, location, participants, note = self.view.input_infos_event()
                new_event = self.model(start_date=start_date, end_date=end_date,location=location,
                                       participants=participants,notes=note)

                session.add(new_event)
                session.commit()
                print("Evenement enregisté !")
                return new_event
            else:
                print("Ce client ne fait pas partie de votre équipe")

        else:
            print("Client non trouvé pour l'ID donné.")
