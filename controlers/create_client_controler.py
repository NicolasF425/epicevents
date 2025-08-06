from controlers.common_controler import CommonControler
from base_managing.CRUD import add_client
from base_managing.models import Client
from utilities.pause import pause


class CreateClientControler(CommonControler):

    def save_new_client(self, datas):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            client = Client()
            client.nom_complet = datas[0]
            client.email = datas[1]
            client.telephone = datas[2]
            client.nom_entreprise = datas[3]
            client.commercial_id = datas[4]
            add_client(client)
            from views.show_clients_view import ShowClientsView
            view = ShowClientsView()
            view.display_clients(filtered=True)
        else:
            from views.login_view import LoginView
            print("Session expirée")
            pause(3)
            view = LoginView()
            view.display_view()
