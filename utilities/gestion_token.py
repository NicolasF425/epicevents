import jwt
import datetime
import json
from typing import Dict, Any, Optional
from utilities.params import SECRET_KEY


class JWTManager:
    def __init__(self, algorithm: str = 'HS256'):
        self.secret_key = SECRET_KEY
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

    def decode_without_verification(self, token) -> Optional[Dict[str, Any]]:
        """Décode un token sans vérification (pour debug)"""
        try:
            decoded = jwt.decode(token, options={"verify_signature": False})
            return decoded
        except Exception as e:
            print(f"Erreur lors du décodage: {e}")
            return None

    def write_token(self, token, filename):
        '''
        Ecrit le token qui expire et le token de refresh dans un fichier
        '''

        f = open(filename, 'w', encoding='utf-8')

        f.write(token)

        f.close()

    def read_token(self, filename):
        '''
        Lit le token à partir du fichier
        '''

        f = open(filename, 'r', encoding='utf-8')

        # lit toutes les lignes et supprime les retours à la ligne
        token = f.readline().strip()

        f.close()

        return token


def main():
    # Configuration
    jwt_manager = JWTManager(SECRET_KEY)

    print("Gestionnaire JWT - Application CLI")
    print("-" * 40)

    while True:
        print("\nActions disponibles:")
        print("1. Créer un token")
        print("2. Vérifier un token")
        print("3. Décoder un token (debug)")
        print("4. Quitter")

        choice = input("\nVotre choix (1-4): ").strip()

        if choice == "1":
            # Créer un token
            print("\nCréation d'un token")
            user_id = input("ID utilisateur: ").strip()
            username = input("Nom d'utilisateur: ").strip()
            role = input("Rôle (admin/user): ").strip() or "user"

            try:
                hours = int(input("Expiration en heures (défaut: 24): ").strip() or "24")
            except ValueError:
                hours = 1

            payload = {
                "user_id": user_id,
                "username": username,
                "role": role
            }

            token = jwt_manager.create_token(payload, hours)
            print("\nToken créé:")
            print(f"{token}")

        elif choice == "2":
            # Vérifier un token
            print("\nVérification d'un token")
            token = input("Entrez le token: ").strip()

            decoded = jwt_manager.verify_token(token)
            if decoded:
                print("\nToken valide!")
                print("📋 Contenu:")
                for key, value in decoded.items():
                    if key in ['exp', 'iat']:
                        # Convertir les timestamps en dates lisibles
                        dt = datetime.datetime.fromtimestamp(value)
                        print(f"   {key}: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
                    else:
                        print(f"   {key}: {value}")

        elif choice == "3":
            # Décoder sans vérification
            print("\n🔧 Décodage sans vérification (debug)")
            token = input("Entrez le token: ").strip()

            decoded = jwt_manager.decode_without_verification(token)
            if decoded:
                print("\n📋 Contenu du token:")
                print(json.dumps(decoded, indent=2, default=str))

        elif choice == "4":
            print("\n👋 Au revoir!")
            break

        else:
            print("❌ Choix invalide")


# Exemple d'utilisation programmatique
def example_usage():
    """Exemple d'utilisation dans votre code"""
    jwt_manager = JWTManager("ma-cle-secrete")

    # Créer un token
    user_data = {
        "user_id": "123",
        "username": "alice",
        "role": "admin"
    }
    token = jwt_manager.create_token(user_data, expires_in_hours=1)
    print(f"Token créé: {token}")

    # Vérifier le token
    decoded = jwt_manager.verify_token(token)
    if decoded:
        print(f"Utilisateur connecté: {decoded['username']}")
        print(f"Rôle: {decoded['role']}")

    return token, decoded


if __name__ == "__main__":
    # Lancer l'interface interactive
    main()

    # Ou utiliser l'exemple programmatique
    # example_usage()
