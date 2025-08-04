from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import COMMERCIAL_COLOR, RESET


class CreateClientView(CommonView):

    def input_datas(self):
        clear_screen()
        print(COMMERCIAL_COLOR+"NOUVEAU CLIENT\n\n"+RESET)

        nom_complet = input("nom complet: ")
        email = input("email: ")
        telephone = input("téléphone: ")
        nom_entreprise = input("nom entreprise: ")
        token = self.check_token_validity()
        if token is not False:
            commercial_id = token["id"]
            datas = [nom_complet, email, telephone, nom_entreprise, commercial_id]
            return datas
        else:
            print("Session expirée")
