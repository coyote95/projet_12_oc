import jwt
from datetime import datetime, timedelta, timezone
import os
from settings.setting import secret_key
from views.base_view import BaseView

current_dir = os.path.dirname(__file__)  # Chemin absolu du répertoire courant
parent_dir = os.path.dirname(current_dir)  # Chemin absolu du répertoire parent


class AuthController(BaseView):
    def __init__(self, user=None):
        self.user = user

    def store_token(self, token):
        try:
            with open(os.path.join(parent_dir, '.token'), 'w') as token_file:
                token_file.write(token)
        except IOError:
            self.display_error_message("Erreur lors de l'écriture du fichier .token")


    def read_token(self):
        try:
            with open(os.path.join(parent_dir, '.token'), 'r') as token_file:
                return token_file.read().strip()
        except IOError:
            self.display_error_message("Erreur lors de la lecture du fichier .token")
            return None

    def generate_token(self):
        # Date et heure actuelles avec un fuseau horaire UTC
        now_utc = datetime.now(timezone.utc)

        # Date d'expiration du JWT (par exemple, 1 heure à partir de maintenant)
        expiration = now_utc + timedelta(hours=1)

        # Création des données à inclure dans le JWT
        payload = {
            'user_id': self.user.id,
            'username': self.user.name,
            'roles': self.user.departement,
            'exp': expiration.timestamp()  # Date d'expiration du token (en secondes)
        }

        # Génération du JWT avec la clé secrète et les données payload
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        self.store_token(token)

        return token

    def valid_token(self):
        token = self.read_token()
        try:
            # Décodage du JWT avec la clé secrète
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            # Le JWT a expiré
            self.display_warning_message("Le jeton a expiré. Vous devez vous réauthentifier.")
            # refreesh login
            return False
        except jwt.InvalidTokenError:
            # Le JWT est invalide
            self.display_error_message("Le jeton est invalide. Veuillez vous reconnecter.")
            return False

    def decode_payload_role_token(self):
        payload = self.valid_token()
        role = payload.get("roles")
        return role

    def decode_payload_id_and_role_token(self):
        payload = self.valid_token()
        role = payload.get("roles")
        id_user = payload.get("user_id")
        return role, id_user
