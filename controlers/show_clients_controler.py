from base_managing.CRUD import get_client_by_id, delete_client
from controlers.common_controler import CommonControler
from views.show_single_client_view import ShowSingleClientView
from views.create_client_view import CreateClientView


class ShowClientsControler(CommonControler):
    """
    Controler for the view ShowClientsView

    Used to manage user's actions
    """

    def select_action(self, action, idClient):
        """
        Manage the action defined in the view

        Args:
            action (string): number of the action
            idClient (string): id of a 'client'
        """

        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if action in ["1", "2", "3"]:
                match action:
                    case "1":  # creation
                        view = CreateClientView()
                        view.input_datas()
                    case "2":  # modification
                        # selection d'une fiche collaborateur
                        client = get_client_by_id(idClient)
                        if client is not False:
                            view = ShowSingleClientView()
                            view.display_single_client(client)
                        else:
                            print("id incorrect !")
                    case "3":
                        delete_client(idClient)
                        print("client supprimé")
                        from views.show_clients_view import ShowClientsView
                        view = ShowClientsView()
                        view.display_clients(filtered=True)
            else:
                # retour au menu
                from views.main_menu_view import MainMenuView
                view = MainMenuView()
                view.display_items()
        else:
            print("Session expirée")
