from utilities.gestion_token import JWTManager
from utilities.params import FILENAME


class CommonView:

    def check_token_validity(self):
        jwt = JWTManager()
        token = jwt.read_token(FILENAME)
        token = jwt.verify_token(token)
        if token is not None:
            return token
        else:
            return False
