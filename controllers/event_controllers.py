from models.clients import Client
from models.events import Event, EventField
from models.contract import Contract
from models.users import User
from views.event_view import EventView
from settings.database import session


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

        if event:  # fonction qui retourne le client.user_id
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

    def read_all_events(self):
        try:
            events = session.query(self.model).all()
            if events:
                for event in events:
                    self.view.display_event(event)
            else:
                print("Aucun event trouvé.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération des contrats : {e}")

    def update_event(self, user_role, user_id):
        event_id = self.view.input_id_contract()
        event = session.query(self.model).filter_by(id=event_id).first()
        if event:
            self.view.display_event(event)

            if user_role == 'gestion':
                answer = self.view.ask_event_update_field_support_id()
                if answer:
                    self.view.input_id_support()
            else:
                if user_id == event.support_id:  # ajouter client
                    field = self.view.ask_event_update_field()
                    if field == EventField.START_DATE.name:
                        new_start_date = self.view.input_start_date()
                        event.start_date = new_start_date
                        session.commit()
                        print("Date de début modifié avec succès.")

                    elif field == EventField.END_DATE:
                        new_end_date = self.view.input_end_date()
                        event.end_date = new_end_date
                        session.commit()
                        print("Date de fin modifié avec succès.")

                    elif field == EventField.LOCATION:
                        new_location = self.view.input_location()
                        event.location = new_location
                        session.commit()
                        print("Statut signature modifié avec succès.")

                    elif field == EventField.PARTICIPANTS:
                        new_participant = self.view.input_participants()
                        event.participants = new_participant
                        session.commit()
                        print("Nombre de participants modifié avec succès.")

                    elif field == EventField.NOTE:
                        new_note = self.view.input_notes()
                        event.notes = new_note
                        session.commit()
                        print("Note modifié avec succès.")

                    elif field == EventField.CONTRACT_ID:
                        new_contrat_id = self.view.input_id_contract()
                        event.contract_id = new_contrat_id
                        session.commit()
                        print("ID contrat modifié avec succès.")

                    elif field == EventField.SUPPORT_ID:
                        new_support_id = self.view.input_id_support()
                        event.support_id = new_support_id
                        session.commit()
                        print("Nombre de participants modifié avec succès.")

            #     else:
            #         print("Option invalide.")
            # else:
            #     print("Ce client ne fait pas partie de votre équipe")
