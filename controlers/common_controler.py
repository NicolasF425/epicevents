from utilities.gestion_token import JWTManager


class CommonControler:
    """
    Controler to be herited

    Used to add the 'check_token_validity' function
    to controlers
    """

    def check_token_validity(self):
        """
        Used to check if the token is valid
        Return the token if valid
        Else return False
        """
        jwt = JWTManager()
        token = jwt.verify_token()
        if token is not None:
            return token
        else:
            return False
