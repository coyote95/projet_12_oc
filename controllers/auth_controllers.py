import jwt
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv
dotenv_path = os.path.join('settings', '.env')
load_dotenv(dotenv_path)

class AuthController:
    def __init__(self, user=None):
        self.user = user

    def store_token(self, token):
        try:
            with open(os.path.join('settings', '.token'), 'w') as token_file:
                token_file.write(token)
        except IOError:
            print("Erreur lors de l'écriture du fichier .token")

    def read_token(self):
        try:
            with open(os.path.join('settings', '.token'), 'r') as token_file:
                return token_file.read().strip()
        except IOError:
            print("Erreur lors de la lecture du fichier .token")
            return None

    def generate_token(self):
        # Lecture de la clé secrète à partir du fichier de configuration
        try:
            secret_key = os.getenv('SECRET_KEY')
        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération de la clé secrète : {e}")

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

    def decode_token(self, token):
        secret_key = os.getenv('SECRET_KEY')

        try:
            # Décodage du JWT avec la clé secrète
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            # Le JWT a expiré
            print("Le jeton a expiré. Vous devez vous réauthentifier.")
            return None
        except jwt.InvalidTokenError:
            # Le JWT est invalide
            print("Le jeton est invalide. Veuillez vous reconnecter.")
            return None
