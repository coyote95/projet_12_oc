import jwt
from datetime import datetime, timedelta, timezone
import configparser


class AuthController:
    def __init__(self, user):
        self.user = user
        self.config = configparser.ConfigParser()

    def store_token(self, token):
        # Lecture du fichier de configuration existant
        self.config.read('config.ini')

        # Ajout du jeton à la section JWT
        if 'JWT' not in self.config:
            self.config['JWT'] = {}
        self.config['JWT']['token'] = token

        # ÉcrituQre des modifications dans le fichier de configuration
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def read_token(self):
        self.config.read('config.ini')
        # Lecture du jeton à partir du fichier de configuration
        if 'JWT' in self.config and 'token' in self.config['JWT']:
            return self.config['JWT']['token']
        else:
            return None

    def generate_token(self):
        self.config.read('config.ini')
        # Lecture de la clé secrète à partir du fichier de configuration
        secret_key = self.config['APP']['SECRET_KEY']

        # Date et heure actuelles avec un fuseau horaire UTC
        now_utc = datetime.now(timezone.utc)

        # Date d'expiration du JWT (par exemple, 1 heure à partir de maintenant)
        expiration = now_utc + timedelta(hours=1)

        # Création des données à inclure dans le JWT
        payload = {
            'user_id': self.user.id,
            'username': self.user.name,
            # 'roles': self.user.role,
            'exp': expiration.timestamp()  # Date d'expiration du token (en secondes)
        }

        # Génération du JWT avec la clé secrète et les données payload
        token = jwt.encode(payload, secret_key, algorithm='HS256')

        self.store_token(token)

        return token

    def decode_token(self, token):
        self.config.read('config.ini')
        # Lecture de la clé secrète à partir du fichier de configuration
        secret_key = self.config['APP']['SECRET_KEY']

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

