from base_managing.CRUD import get_all_clients
from views.common_view import CommonView
from utilities.clear_screen import clear_screen


class ShowClientsView(CommonView):

    def display_clients(self):
        clients = get_all_clients()

        clear_screen()

        for client in clients:
            id = client.id
            entreprise = client.nom_entreprise
            print(str(id)+" "+entreprise)
