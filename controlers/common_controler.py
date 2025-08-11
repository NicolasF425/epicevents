from utilities.gestion_token import JWTManager


class CommonControler:

    def check_token_validity(self):
        jwt = JWTManager()
        token = jwt.verify_token()
        if token is not None:
            return token
        else:
            return False
