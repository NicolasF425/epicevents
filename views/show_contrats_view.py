from base_managing.CRUD import get_all_contrats, get_client_by_id
from views.common_view import CommonView
from utilities.clear_screen import clear_screen


class ShowContratsView(CommonView):

    def display_contrats(self):
        clear_screen()
        token = self.check_token_validity()

        if token is not False:
            print("CONTRATS\n\n")
            contrats = get_all_contrats()
            for contrat in contrats:
                id = contrat.id
                client = contrat.client_id
                nom_client = get_client_by_id(client).nom_entreprise
                print(f"{"║ "+str(id)[:5]:<5} | {nom_client[:30]:<30} ║")
            print("\n 1) Créer un nouveau contrat")
            print(" 2) Modifier un contrat")
            print(" 3) Supprimer un contrat")
            choix = input("\nEntrez le numéro d'une action "
                          "ou appuyez sur Entrée pour retourner au menu : ")
            if choix == "1":
                contrat = 0
            elif choix == "2":
                contrat = input("Entrez l'id du contrat à modifier: ")
            elif choix == "3":
                contrat = input("Entrez l'id du collaborateur à supprimer: ")
            else:
                choix = ""
                contrat = 0

        else:
            print("Session expirée")
