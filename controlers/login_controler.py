from base_managing.CRUD import get_collaborateur_by_login
from utilities.gestion_token import JWTManager
from utilities.gestion_hashage import verify_password
from views.main_menu_view import MainMenuView
import os
import sentry_sdk


class LoginControler:

    def check_credentials(self, login, password):
        user = get_collaborateur_by_login(login)
        if user is not None:
            # vérification du mot de passe
            if verify_password(password, user.password):
                # création du token
                jwt = JWTManager()
                payload = {
                    'login': user.login,
                    'id': user.id,
                    'departement_id': user.departement_id
                }
                tokens = jwt.create_tokens(payload)
                jwt.write_tokens(tokens, os.getenv("FILENAME"))
                sentry_sdk.set_user({
                    "id": user.id,          # ID unique de l'utilisateur
                    "username": user.login,  # Nom d'utilisateur
                })
                view = MainMenuView()
                view.display_items()
            else:
                print('login ou mot de passe incorrect')
        else:
            print('login ou mot de passe incorrect')
