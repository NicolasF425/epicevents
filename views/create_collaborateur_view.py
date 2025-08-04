from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import GESTION_COLOR, RESET
from utilities.gestion_hashage import hash_password


class CreateCollaborateurView(CommonView):

    def input_datas():
        clear_screen()
        print(GESTION_COLOR+"NOUVEAU COLLABORATEUR"+RESET)

        login = input("login: ")
        password = input("mot de passe: ")
        password = hash_password(password)
        email = input("email: ")
        OK = False
        while not OK:
            try:
                departement_id = input("id du departement (1/2/3)")
                departement_id = int(departement_id)
                if departement_id < 1 and departement_id > 3:
                    print("Veuillez entrer une valeur entre 1 et 3")
                else:
                    OK = True
            except ValueError:
                print("Veuillez entrer une valeur numérique")

        datas = [login, password, email, departement_id]
        return datas
