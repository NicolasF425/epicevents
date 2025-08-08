import jwt
import datetime
from typing import Dict, Any, Optional
import os


class JWTManager:

    filename = os.getenv("FILENAME")

    def __init__(self, algorithm: str = 'HS256'):
        self.secret_key = os.getenv("SECRET_KEY")
        self.algorithm = algorithm

    def create_token(self, payload: Dict[str, Any], expires_in_hours: int = 1):
        """Crée un token JWT avec une expiration"""
        # Ajouter l'expiration au payload
        payload_copy = payload.copy()
        payload_copy['exp'] = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=expires_in_hours)
        payload_copy['iat'] = datetime.datetime.now(datetime.timezone.utc)

        # Encoder le token
        token = jwt.encode(payload_copy, self.secret_key, algorithm=self.algorithm)
        return token

    def renew_token():
        pass

    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Vérifie et décode un token JWT"""
        try:
            decoded = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return decoded
        except jwt.ExpiredSignatureError:
            print("Token expiré")
            return None
        except jwt.InvalidTokenError:
            print("Token invalide")
            return None

    def write_token(self, token, filename):
        '''
        Ecrit le token dans un fichier
        '''
        f = open(filename, 'w', encoding='utf-8')
        f.write(token)
        f.close()

    def read_token(self, filename):
        '''
        Lit le token à partir du fichier
        '''
        f = open(filename, 'r', encoding='utf-8')
        token = f.readline().strip()
        f.close()
        return token
