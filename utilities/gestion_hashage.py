from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def hash_password(password):
    """Hache un mot de passe"""
    ph = PasswordHasher()
    return ph.hash(password)


def verify_password(password, hashed_password):
    """Vérifie si un mot de passe correspond au hash"""
    try:
        ph = PasswordHasher()
        ph.verify(hashed_password, password)
        return True
    except VerifyMismatchError:
        return False
