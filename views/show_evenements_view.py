from base_managing.CRUD import get_all_evenements, get_evenements_by_idSupport
from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import GREEN, RESET


class ShowEvenementsView(CommonView):

    def display_evenements(self, filtered=False):
        clear_screen()
        token = self.check_token_validity()

        if token is not False:
            if not filtered:
                print(GREEN+"EVENEMENTS\n\n"+RESET)
                evenements = get_all_evenements()
            else:
                print("MES EVENEMENTS\n\n")
                evenements = get_evenements_by_idSupport()
            for evenement in evenements:
                id = evenement.id
                nom = evenement.nom
                print(f"{"║ "+str(id)[:5]:<5} | {nom[:40]:<40} ║")
            print("\n 1) Créer un nouvel événement")
            print(" 2) Modifier un événement")
            print(" 3) Supprimer un événement")
            choix = input("\nEntrez le numéro d'une action "
                          "ou appuyez sur Entrée pour retourner au menu : ")
            if choix == "1":
                evenement = 0
            elif choix == "2":
                evenement = input("Entrez l'id de l'événement à modifier: ")
            elif choix == "3":
                evenement = input("Entrez l'id de l'événement à supprimer: ")
            else:
                choix = ""
                evenement = 0

        else:
            print("Session expirée")
