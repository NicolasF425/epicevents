from utilities.gestion_token import JWTManager
import os


class CommonView:

    def check_token_validity(self):
        jwt = JWTManager()
        token = jwt.read_token(os.getenv("FILENAME"))
        token = jwt.verify_token(token)
        if token is not None:
            return token
        else:
            return False
