from base_managing.CRUD import get_client_by_id
from controlers.common_controler import CommonControler
from views.show_single_client_view import ShowSingleClientView
from views.create_client_view import CreateClientView
from base_managing.CRUD import delete_client


class ShowClientsControler(CommonControler):

    def select_action(self, action, idClient):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if idClient != "":
                match action:
                    case 1:  # creation
                        view = CreateClientView()
                        view.input_datas()
                    case 2:  # modification
                        # selection d'une fiche collaborateur
                        client = get_client_by_id(idClient)
                        if client is not False:
                            view = ShowSingleClientView()
                            view.display_single_client(client)
                        else:
                            print("id incorrect !")
                    case 3:  # suppression
                        delete_client(idClient)
            else:
                # retour au menu
                from views.main_menu_view import MainMenuView
                view = MainMenuView()
                view.display_items()
        else:
            print("Session expirée")
