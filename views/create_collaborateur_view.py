from views.common_view import CommonView
from controlers.create_collaborateur_controler import CreateCollaborateurControler
from utilities.clear_screen import clear_screen
from utilities.pause import pause
from utilities.constantes import GESTION_COLOR, RESET
from utilities.gestion_hashage import hash_password


class CreateCollaborateurView(CommonView):
    controler = CreateCollaborateurControler()

    def input_datas(self):
        clear_screen()
        print(GESTION_COLOR+"NOUVEAU COLLABORATEUR"+RESET)

        login = input("login: ")
        password = input("mot de passe: ")
        password = hash_password(password)
        email = input("email: ")
        departement_id = ""
        while departement_id not in ["1", "2", "3"]:
            departement_id = input("id du departement (1/2/3): ")
        departement_id = int(departement_id)
        datas = [login, password, email, departement_id]
        token = self.check_token_validity()

        if token is not False:
            self.controler.save_new_collaborateur(datas)
        else:
            from views.login_view import LoginView
            print("Session expirée")
            pause(3)
            view = LoginView()
            view.display_view()
