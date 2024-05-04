from models.events import Event, EventField
from models.contract import Contract
from models.users import User
from views.event_view import EventView
from settings.database import session


class EventController:
    def __init__(self):
        self.model = Event
        self.view = EventView

    def create_event(self, user_id):
        contract_id = self.view.input_id_contract()
        contract = Contract.filter_by_id(contract_id)
        if contract:
            event = Event.filter_by_contract_id(contract_id)
            if not event:
                if contract.client.get_commercial_id() == user_id:
                    if contract.signed:
                        start_date = self.view.input_start_date()
                        while True:
                            end_date = self.view.input_end_date()
                            if end_date > start_date:
                                break
                            else:
                                self.view.display_error_message("La date de fin doit être postérieure à la date de début.")

                        location, participants, note = self.view.input_infos_event()
                        new_event = self.model(start_date=start_date, end_date=end_date, location=location,
                                               participants=participants, notes=note)
                        new_event.set_contract_id(contract_id)
                        support_id = self.view.input_id_support()
                        user = User.filter_by_id(support_id)
                        if user:
                            if user.get_departement() == 'support':
                                new_event.set_support_id(support_id)
                            else:
                                self.view.display_warning_message("Cet utilitateur ne fait pas parti de l'équipe support")
                        else:
                            self.view.display_warning_message("cette utilisateur n'existe pas")

                        session.add(new_event)
                        session.commit()
                        self.view.display_info_message("Evenement enregisté !")
                        return new_event
                    else:
                        self.view.display_warning_message("Ce client n'a pas encore signé le contrat")
                else:
                    self.view.display_warning_message("Ce client ne fait pas partie de votre équipe")
            else:
                self.view.display_warning_message("Un événement est déjà associé à ce contrat")
        else:
            self.view.display_warning_message("Contrat non trouvé pour l'ID donné.")

    def delete_event_by_id(self, user_id):
        event_id = self.view.input_id_event()
        event = self.model.filter_by_event_id(event_id)
        if event:
            commercial_id = self.model.find_commercial_id(event_id)
            if commercial_id == user_id:
                session.delete(event)
                session.commit()
                self.view.display_info_message("Evénement supprimé avec succès.")
            else:
                self.view.display_warning_message("Ce client ne fait pas partie de votre équipe")
        else:
            self.view.display_warning_message("Evenement non trouvé.")

    def read_all_events(self):
        try:
            events = Event.filter_all_events()
            if events:
                for event in events:
                    self.view.display_event(event)
            else:
                self.view.display_warning_message("Aucun événement trouvé.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération des événements : {e}")

    def update_event(self, user_role, user_id):
        event_id = self.view.input_id_contract()
        event = Event.filter_by_event_id(event_id)
        if event:
            self.view.display_event(event)

            if user_role == 'gestion':
                support_id = self.view.ask_event_update_field_support_id()
                if support_id:
                    self.view.input_id_support()
                    event.set_support_id(support_id)
                    session.commit()
                    self.view.display_info_message("Contact support modifié avec succès.")

            else:
                if event.get_support_id() == user_id:
                    field = self.view.ask_event_update_field()
                    if field == EventField.START_DATE.name:
                        new_start_date = self.view.input_start_date()
                        event.set_start_date(new_start_date)
                        session.commit()
                        self.view.display_info_message("Date de début modifié avec succès.")


                    elif field == EventField.END_DATE:
                        new_end_date = self.view.input_end_date()
                        event.set_end_date(new_end_date)
                        session.commit()
                        self.view.display_info_message("Date de fin modifié avec succès.")


                    elif field == EventField.LOCATION:
                        new_location = self.view.input_location()
                        event.set_location(new_location)
                        session.commit()
                        self.view.display_info_message("Statut signature modifié avec succès.")


                    elif field == EventField.PARTICIPANTS:
                        new_participant = self.view.input_participants()
                        event.set_participants(new_participant)
                        session.commit()
                        self.view.display_info_message("Nombre de participants modifié avec succès.")


                    elif field == EventField.NOTE:
                        new_note = self.view.input_notes()
                        event.set_notes(new_note)
                        session.commit()
                        self.view.display_info_message("Note modifié avec succès.")


                    elif field == EventField.CONTRACT_ID:
                        new_contrat_id = self.view.input_id_contract()
                        event.set_contract_id(new_contrat_id)
                        session.commit()
                        self.view.display_info_message("ID contrat modifié avec succès.")

                    elif field == EventField.SUPPORT_ID:
                        new_support_id = self.view.input_id_support()
                        event.set_support_id(new_support_id)
                        session.commit()
                        self.view.display_info_message("Nombre de participants modifié avec succès.")
                        print()

                    else:
                        self.view.display_warning_message("Option invalide.")

                else:
                    self.view.display_warning_message("Ce client ne fait pas partie de votre équipe")


    def filter_events(self, user_role, user_id):
        if user_role == 'support':
            self.view.filter_message("Voici la liste de vos événements:")
            try:
                events = self.model.filter_by_support(user_id)
                if events:
                    for event in events:
                        self.view.display_event(event)
                else:
                    self.view.display_info_message("Aucun événement trouvé.")
            except Exception as e:
                self.view.display_error_message(f"Une erreur s'est produite lors de la récupération des événements :"
                                                f" {e}")

        elif user_role == 'gestion':
            self.view.filter_message("Voici la liste des événements sans support:")
            try:
                events = self.model.filter_by_none_support()
                if events:
                    for event in events:
                        self.view.display_event(event)
                else:
                    self.view.display_info_message("Aucun événement trouvé.")
            except Exception as e:
                self.view.display_error_message(f"Une erreur s'est produite lors de la récupération des événements :"
                                                f" {e}")
        else:
            self.view.display_info_message("Aucun filtre événement disponible")
