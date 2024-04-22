import jwt
from datetime import datetime, timedelta, timezone


class AuthController:

    def __init__(self, user_service):
        self.user_service = user_service

    def generate_jwt(self, user_id, username, roles):
        # Clé secrète pour signer le JWT (à conserver en sécurité)
        secret_key = "your_secret_key"

        # Date et heure actuelles avec un fuseau horaire UTC
        now_utc = datetime.now(timezone.utc)

        # Date d'expiration du JWT (par exemple, 1 heure à partir de maintenant)
        expiration = now_utc + timedelta(hours=1)

        # Création des données à inclure dans le JWT
        payload = {
            'user_id': user_id,
            'username': username,
            'roles': roles,
            'exp': expiration  # Date d'expiration du token
        }

        # Génération du JWT avec la clé secrète et les données payload
        token = jwt.encode(payload, secret_key, algorithm='HS256')

        return token

    def decode_jwt(self, token):
        # Clé secrète utilisée pour vérifier le JWT
        secret_key = "your_secret_key"

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

    def login(self, username, password):
        # Authentification de l'utilisateur et génération du JWT
        user = self.user_service.get_user_by_username(username)

        if user and user.check_password(password):
            roles = user.get_roles()  # Récupérer les rôles de l'utilisateur depuis le modèle User
            token = self.generate_jwt(user.id, user.username, roles)
            return token
        else:
            return None

    def logout(self):
        pass
