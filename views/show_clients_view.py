from base_managing.CRUD import get_all_clients
from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from controlers.show_clients_controler import ShowClientsControler


class ShowClientsView(CommonView):
    controler = ShowClientsControler()

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
            id_client = input("Entrez le numéro de client ou appuyez "
                              "sur Entrée pour retourner au menu : ")
            self.controler.select_action(id_client)
        else:
            print("Session expirée")
