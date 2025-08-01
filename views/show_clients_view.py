from base_managing.CRUD import get_all_clients
from views.common_view import CommonView
from utilities.clear_screen import clear_screen


class ShowClientsView(CommonView):

    def display_clients(self):
        clear_screen()
        token = self.check_token_validity()

        if token is not False:
            print("CLIENTS\n\n")
            clients = get_all_clients()
            for client in clients:
                id = client.id
                entreprise = client.nom_entreprise
                print(f"{"║ "+str(id)[:5]:<5} | {entreprise[:30]:<30} ║")
            input("")
        else:
            print("Session expirée")
