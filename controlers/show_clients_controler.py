from base_managing.CRUD import get_client_by_id
from controlers.common_controler import CommonControler
from views.show_single_client_view import ShowSingleClientView


class ShowClientsControler(CommonControler):

    def select_action(self, id_client):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if id_client != "":
                id_client = int(id_client)
                # selection d'une fiche collaborateur
                client = get_client_by_id(id_client)
                if client is not False:
                    view = ShowSingleClientView()
                    view.display_single_client(client)
                else:
                    print("id incorrect !")
            else:
                # retour au menu
                from views.main_menu_view import MainMenuView
                view = MainMenuView()
                view.display_items()
        else:
            print("Session expirée")
