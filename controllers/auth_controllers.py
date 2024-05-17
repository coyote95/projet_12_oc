"""
AuthController module for handling user authentication and JWT token operations.

Classes:
    AuthController: Inherits from BaseView for print message.

Methods:
    __init__(self, user=None):
        Initializes the AuthController with an optional user.

    store_token(self, token):
        Stores the given token in a file.

    read_token(self):
        Reads the stored token from a file.

    generate_token(self):
        Generates a JWT token for the current user and stores it.

    valid_token(self):
        Validates the stored JWT token and returns the payload if valid.

    decode_payload_id_and_role_token(self):
        Decodes the user ID and roles from the token payload.
"""

import jwt
from datetime import datetime, timedelta, timezone
import os
from settings.setting import secret_key
from views.base_view import BaseView

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)


class AuthController(BaseView):
    def __init__(self, user=None):
        self.user = user

    def store_token(self, token):
        try:
            with open(os.path.join(parent_dir, ".token"), "w") as token_file:
                token_file.write(token)
        except IOError:
            self.display_error_message("Erreur lors de l'écriture du fichier .token")

    def read_token(self):
        try:
            with open(os.path.join(parent_dir, ".token"), "r") as token_file:
                return token_file.read().strip()
        except IOError:
            self.display_error_message("Erreur lors de la lecture du fichier .token")
            return None

    def generate_token(self):
        now_utc = datetime.now(timezone.utc)
        expiration = now_utc + timedelta(hours=1)
        payload = {
            "user_id": self.user.id,
            "username": self.user.name,
            "roles": self.user.departement,
            "exp": expiration.timestamp(),
        }
        token = jwt.encode(payload, secret_key, algorithm="HS256")
        self.store_token(token)
        return token

    def valid_token(self):
        token = self.read_token()
        try:
            payload = jwt.decode(token, secret_key, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            self.display_warning_message(
                "Le jeton a expiré. Vous devez vous réauthentifier."
            )
            return False
        except jwt.InvalidTokenError:
            self.display_error_message(
                "Le jeton est invalide. Veuillez vous reconnecter."
            )
            return False

    # def decode_payload_role_token(self):
    #     payload = self.valid_token()
    #     role = payload.get("roles")
    #     return role

    def decode_payload_id_and_role_token(self):
        payload = self.valid_token()
        role = payload.get("roles")
        id_user = payload.get("user_id")
        return role, id_user
