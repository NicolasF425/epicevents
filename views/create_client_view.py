from views.common_view import CommonView
from controlers.create_client_controler import CreateClientControler
from utilities.clear_screen import clear_screen
from utilities.pause import pause
from utilities.constantes import COMMERCIAL_COLOR, RESET


class CreateClientView(CommonView):
    controler = CreateClientControler()

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
            self.controler.save_new_client(datas)
        else:
            from views.login_view import LoginView
            print("Session expirée")
            pause(3)
            view = LoginView()
            view.display_view()
