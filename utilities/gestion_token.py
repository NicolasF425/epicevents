import os
import json
import jwt
import datetime
from typing import Optional, Dict, Any


class JWTManager:
    """
    Class for managing the token creation, refresh and validity
    """

    def __init__(self, algorithm: str = 'HS256'):
        self.secret_key = os.getenv("SECRET_KEY")
        self.algorithm = algorithm
        self.filename = os.getenv("FILENAME", "tokens.json")  # Valeur par défaut

    def create_tokens(self, payload: Dict[str, Any]):
        """Crée un access token et un refresh token"""
        now = datetime.datetime.now(datetime.timezone.utc)

        # Access token (courte durée)
        access_payload = payload.copy()
        access_payload['exp'] = now + datetime.timedelta(minutes=10)
        access_payload['iat'] = now
        access_payload['type'] = 'access'

        access_token = jwt.encode(access_payload, self.secret_key, algorithm=self.algorithm)

        # Refresh token (longue durée)
        refresh_payload = {
            'id': payload.get('id'),
            'departement_id': payload.get('departement_id'),
            'exp': now + datetime.timedelta(days=1),
            'iat': now,
            'type': 'refresh'
        }

        refresh_token = jwt.encode(refresh_payload, self.secret_key, algorithm=self.algorithm)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def refresh_access_token(self, refresh_token: str):
        """Rafraîchit les tokens en utilisant le refresh token"""
        try:
            # Décoder et valider le refresh token
            payload = jwt.decode(refresh_token, self.secret_key, algorithms=[self.algorithm])

            if payload.get('type') != 'refresh':
                raise ValueError("Token invalide - type incorrect")

            if not payload.get('id'):
                raise ValueError("Token invalide - id user manquant")

            # Créer de nouveaux tokens
            new_payload = {
                'id': payload['id'],
                'departement_id': payload['departement_id']
            }

            return self.create_tokens(new_payload)  # CORRIGÉ: était create_token

        except jwt.ExpiredSignatureError:
            raise ValueError("Refresh token expiré")
        except jwt.InvalidTokenError:
            raise ValueError("Refresh token invalide")

    def verify_token(self, token: str = None, filename: str = None) -> Optional[Dict[str, Any]]:
        """
        Vérifie et décode un token JWT avec gestion automatique du refresh

        Args:
            token: Token à vérifier (optionnel, sera lu depuis le fichier si non fourni)
            filename: Nom du fichier contenant les tokens (utilise self.filename par défaut)

        Returns:
            Dict avec les données décodées du token ou None si invalide
        """
        if filename is None:
            filename = self.filename

        # Si aucun token fourni, lire depuis le fichier
        if token is None:
            try:
                tokens = self.read_tokens(filename)
                token = tokens.get('access_token')
                if not token:
                    print("Aucun access token trouvé dans le fichier")
                    return None
            except (FileNotFoundError, ValueError) as e:
                print(f"Erreur lecture fichier: {e}")
                return None

        # Essayer de vérifier le token
        try:
            decoded = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return decoded

        except jwt.ExpiredSignatureError:
            print("Access token expiré, tentative de refresh...")

            # Essayer de rafraîchir automatiquement
            refreshed_tokens = self._auto_refresh_token(filename)
            if refreshed_tokens:
                # Retourner les données décodées du nouveau token
                try:
                    return jwt.decode(refreshed_tokens['access_token'], self.secret_key, algorithms=[self.algorithm])
                except jwt.InvalidTokenError:
                    print("Erreur avec le nouveau token")
                    return None
            else:
                print("Impossible de rafraîchir le token")
                return None

        except jwt.InvalidTokenError:
            print("Token invalide")
            return None

    def _auto_refresh_token(self, filename: str = None) -> Optional[Dict[str, str]]:
        """
        Méthode privée pour rafraîchir automatiquement le token

        Args:
            filename: Nom du fichier contenant les tokens

        Returns:
            Nouveaux tokens ou None si échec
        """
        if filename is None:
            filename = self.filename

        try:
            # Lire les tokens existants
            tokens = self.read_tokens(filename)
            refresh_token = tokens.get('refresh_token')

            if not refresh_token:
                print("Aucun refresh token disponible")
                return None

            # Rafraîchir les tokens
            new_tokens = self.refresh_access_token(refresh_token)

            # Sauvegarder les nouveaux tokens
            self.write_tokens(new_tokens, filename)

            return new_tokens

        except Exception as e:
            print(f"Erreur lors du refresh automatique: {e}")
            return None

    def is_token_valid(self, filename: str = None) -> bool:
        """
        Vérifie rapidement si les tokens sont valides (avec refresh automatique)

        Args:
            filename: Nom du fichier contenant les tokens

        Returns:
            True si un token valide est disponible (après refresh si nécessaire)
        """
        if filename is None:
            filename = self.filename

        result = self.verify_token(filename=filename)
        return result is not None

    def get_user_from_token(self, filename: str = None) -> Optional[int]:
        """
        Récupère l'ID utilisateur depuis le token (avec refresh automatique)

        Args:
            filename: Nom du fichier contenant les tokens

        Returns:
            ID utilisateur ou None si token invalide
        """
        if filename is None:
            filename = self.filename

        token_data = self.verify_token(filename=filename)
        if token_data:
            return token_data.get('id')
        return None

    def write_tokens(self, tokens_dict: Dict[str, str], filename: str = None):
        """
        Écrit les tokens dans un fichier JSON
        """
        if filename is None:
            filename = self.filename

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(tokens_dict, f, indent=2)

    def read_tokens(self, filename: str = None) -> Dict[str, str]:
        """
        Lit les tokens à partir du fichier JSON
        """
        if filename is None:
            filename = self.filename

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                tokens = json.load(f)
            return tokens

        except FileNotFoundError:
            raise FileNotFoundError(f"Fichier token non trouvé: {filename}")
        except json.JSONDecodeError:
            raise ValueError(f"Fichier JSON invalide: {filename}")

    def read_specific_token(self, token_type: str, filename: str = None) -> Optional[str]:
        """
        Lit un type de token spécifique
        """
        if filename is None:
            filename = self.filename

        tokens = self.read_tokens(filename)

        if token_type == 'access':
            return tokens.get('access_token')
        elif token_type == 'refresh':
            return tokens.get('refresh_token')
        else:
            raise ValueError("Type de token invalide. Utilisez 'access' ou 'refresh'")

    def logout(self, filename: str = None):
        """
        Supprime les tokens (déconnexion)
        """
        if filename is None:
            filename = self.filename

        try:
            os.remove(filename)
            print("Déconnexion réussie")
        except FileNotFoundError:
            print("Aucun token à supprimer")

    def get_token_info(self, filename: str = None) -> Optional[Dict[str, Any]]:
        """
        Récupère les informations sur les tokens sans les valider
        """
        if filename is None:
            filename = self.filename

        try:
            tokens = self.read_tokens(filename)

            info = {}

            # Info sur l'access token
            try:
                access_payload = jwt.decode(tokens.get('access_token', ''),
                                            self.secret_key,
                                            algorithms=[self.algorithm],
                                            options={"verify_exp": False})
                info['access_token'] = {
                    'id': access_payload.get('id'),
                    'expires': datetime.datetime.fromtimestamp(access_payload.get('exp', 0), tz=datetime.timezone.utc),
                    'type': access_payload.get('type')
                }
            except ValueError:
                info['access_token'] = None

            # Info sur le refresh token
            try:
                refresh_payload = jwt.decode(tokens.get('refresh_token', ''),
                                             self.secret_key,
                                             algorithms=[self.algorithm],
                                             options={"verify_exp": False})
                info['refresh_token'] = {
                    'id': refresh_payload.get('id'),
                    'expires': datetime.datetime.fromtimestamp(refresh_payload.get('exp', 0),
                                                               tz=datetime.timezone.utc),
                    'type': refresh_payload.get('type')
                }
            except ValueError:
                info['refresh_token'] = None

            return info

        except Exception as e:
            print(f"Erreur lors de la lecture des infos token: {e}")
            return None
