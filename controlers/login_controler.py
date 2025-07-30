from base_managing.CRUD import get_collaborateur_by_login
from utilities.gestion_token import JWTManager
from utilities.gestion_hashage import hash_password, verify_password


class LoginControler:

    def check_credentials(login, password):
        user = get_collaborateur_by_login(login)
        if user is not None:
            # vérification du mot de passe
            print(user.password)
            print(hash_password(password))
            if verify_password(password, user.password):
                # création du token
                jwt = JWTManager()
                payload = {
                    'login': user.login,
                    'id': user.id,
                    'departement_id': user.departement_id
                }
                token = jwt.create_token(payload)
                jwt.write_token(token, "token.txt")
                loaded_token = jwt.read_token("token.txt")
                decoded_token = jwt.verify_token(loaded_token)
                print(decoded_token)
            else:
                print('login ou mot de passe incorrect')
        else:
            print('utilisateur non trouvé')
