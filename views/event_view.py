from datetime import datetime
from models.events import EventField


class EventView:

    @staticmethod
    def afficher_message(message):
        print(message)

    @staticmethod
    def input_id_contract():
        while True:
            contract_id = input("Entrez l'id du contrat: ")
            try:
                contract_id = int(contract_id)
                return contract_id
            except ValueError:
                print("Vous n'avez pas écrit un entier.")

    @staticmethod
    def input_start_date():
        while True:
            start_date = input("Entrez la date de début de l'événement (YYYY-MM-DD HH:MM): ")
            start_date += ":00"
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
                return start_date
            except ValueError:
                print("Format de date incorrect. Utilisez le format YYYY-MM-DD HH:MM.")



    @staticmethod
    def input_end_date():
        while True:
            end_date = input("Entrez la date de fin de l'événement (YYYY-MM-DD HH:MM): ")
            end_date += ":00"
            try:
                end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
                return end_date
            except ValueError:
                print("Format de date incorrect. Utilisez le format YYYY-MM-DD HH:MM.")


    @staticmethod
    def input_location():
        location = input("Entrez le lieu de l'événement: ")
        return location.upper()

    @staticmethod
    def input_notes():
        while True:
            notes = input("Entrez une note: ")
            if len(notes) < 255:
                return notes
            else:
                print("Veuillez reduire la taille de votre note")

    @staticmethod
    def input_participants():
        while True:
            participants = input("Entrez le nombre de particpants: ")
            try:
                participants = int(participants)
                return participants
            except ValueError:
                print("Vous n'avez pas écrit un entier.")

    @staticmethod
    def input_id_event():
        while True:
            event_id = input("Entrez l'id de l'événement: ")
            try:
                event_id = int(event_id)
                return event_id
            except ValueError:
                print("Vous n'avez pas écrit un entier.")

    @staticmethod
    def input_id_support():
        while True:
            support_id = input("Entrez l'id support: ")
            try:
                support_id = int(support_id)
                return support_id
            except ValueError:
                print("Vous n'avez pas écrit un entier.")

    @staticmethod
    def input_infos_event():
        location = EventView.input_location()
        participants = EventView.input_participants()
        note = EventView.input_notes()
        return  location, participants, note

    @staticmethod
    def display_event(event):
        print(
            f"id:{event.get_id()}    "
            f"Date de début:{event.get_start_date()}    "
            f"Date de fin:{event.get_end_date()}    "
            f"Localisation:{event.get_location()}    "
            f"Nombre de participants:{event.get_participants()}    "
            f"Note:{event.get_notes()}    "
            f"Contact support: {event.get_support()}    "
            f"Contrat:{event.get_contract()}"

        )

    @staticmethod
    def ask_event_update_field_support_id():
        while True:
            answer = input("Voulez-vous modifier le support id de l'evenement (oui/non)?")
            if answer == 'oui':
                return True
            elif answer == 'non':
                return False



    @staticmethod
    def ask_event_update_field():
        while True:
            try:
                choice = int(input(
                    f"Quelle information voulez-vous modifier?\n"
                    f"1: {EventField.START_DATE.name}\n"
                    f"2: {EventField.END_DATE.name}\n"
                    f"3: {EventField.LOCATION.name}\n"
                    f"4: {EventField.PARTICIPANTS.name}\n"
                    f"5: {EventField.NOTE.name}\n"
                    f"6: {EventField.CONTRACT_ID.name}\n"
                    f"7: {EventField.SUPPORT_ID.name}\n"
                ))
                field = EventField(choice)
                if field in EventField:
                    return field
                else:
                    print("Vous n'avez pas écrit un numéro valide.")
            except ValueError:
                print("Vous devez entrer un entier.")