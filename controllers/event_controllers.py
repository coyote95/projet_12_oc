from models.clients import Client
from models.events import Event
from models.contract import Contract
from models.users import User
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
            event = session.query(Event).filter_by(contract_id=contract_id).first()
            if not event:
                if contrat.client.user_id == user_id:
                    start_date, end_date, location, participants, note = self.view.input_infos_event()
                    new_event = self.model(start_date=start_date, end_date=end_date, location=location,
                                           participants=participants, notes=note)
                    new_event.contract_id = contract_id
                    support_id = self.view.input_id_support()
                    user = session.query(User).filter_by(id=support_id).first()
                    if user:
                        if user.get_departement() == 'support':
                            new_event.support_id = support_id
                        else:
                            print("Cet utilitateur ne fait pas parti de l'équipe support")
                    else:
                        print("cette utilisateur n'existe pas")

                    session.add(new_event)
                    session.commit()
                    print("Evenement enregisté !")
                    return new_event
                else:
                    print("Ce client ne fait pas partie de votre équipe")
            else:
                print("Un événement est déjà associé à ce contrat")
        else:
            print("Contrat non trouvé pour l'ID donné.")

    def delete_event_by_id(self, user_role, user_id):
        event_id = self.view.input_id_event()
        event = session.query(Event).filter_by(id=event_id).first()

        if event:
            self.view.display_event(event)
            contract = session.query(Contract).filter_by(id=event.contract_id).first()
            if contract:
                client = session.query(Client).filter_by(id=contract.client_id).first()
                if client:
                    if client.user_id == user_id:
                        session.delete(event)
                        session.commit()
                        print("Event supprimé avec succès.")
                    else:
                        print("Error suppression événement: Ce client ne fait pas partie de votre équipe")
        else:
            print("Evenement non trouvé.")
