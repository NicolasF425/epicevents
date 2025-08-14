from base_managing.CRUD import get_all_clients, get_clients_by_idCommercial
from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import BLUE, RESET
from controlers.show_clients_controler import ShowClientsControler


class ShowClientsView(CommonView):
    controler = ShowClientsControler()

    def display_clients(self, filtered=False):
        clear_screen()
        token = self.check_token_validity()

        if token is not False:
            if not filtered:
                print("CLIENTS\n\n")
                clients = get_all_clients()
            else:
                print(BLUE+"MES CLIENTS\n\n"+RESET)
                clients = get_clients_by_idCommercial(int(token["id"]))
            ids_clients = []
            for client in clients:
                id = client.id
                ids_clients.append(id)
                entreprise = client.nom_entreprise
                print(f"{"║ "+str(id)[:5]:<5} | {entreprise[:30]:<30} ║")
            if not filtered:
                print("\n 1) Voir un client")
                choix = input("ou appuyez sur Entrée pour retourner au menu : ")
                if choix == "1":
                    client = input("Entrez l'id du client: ")
                    choix = "2"
                else:
                    choix = ""
                    client = 0
            else:
                print("\n 1) Créer un nouveau client")
                print(" 2) Voir ou modifier un client")
                choix = input("\nEntrez le numéro d'une action "
                              "ou appuyez sur Entrée pour retourner au menu : ")
                if choix == "1":
                    client = 0
                elif choix == "2":
                    client = input("Entrez l'id du client: ")
                    int_client = int(client)
                    if int_client not in ids_clients:
                        print("id incorrect")
                        client = 0
                    else:
                        client = int_client
                else:
                    choix = ""
                    client = 0
            self.controler.select_action(choix, client)
        else:
            print("Session expirée")
