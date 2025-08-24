from controlers.common_controler import CommonControler
from base_managing.CRUD import update_client, get_client_by_id


class ShowSingleClientControler(CommonControler):
    """
    Controler for the view ShowSingleClientView

    Use to manage user's actions
    """

    def check_action(self, action, id):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if action != "":
                # modification d'un champ
                from views.show_single_client_view import ShowSingleClientView
                view = ShowSingleClientView()
                action = int(action)
                view.display_update(id, action)
            else:
                # retour à la liste des clients
                from views.show_clients_view import ShowClientsView
                view = ShowClientsView()
                view.display_clients()
        else:
            print("Session expirée")

    def save_new_value(self, idClient, field, value):
        if idClient > 0:
            update_client(idClient, field, value)
            from views.show_single_client_view import ShowSingleClientView
            view = ShowSingleClientView()
            client = get_client_by_id(idClient)
            view.display_single_client(client)
