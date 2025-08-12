from base_managing.CRUD import get_all_evenements, get_evenements_by_idSupport, get_evenements_without_support
from views.common_view import CommonView
from controlers.show_evenements_controler import ShowEvenementsControler
from utilities.clear_screen import clear_screen
from utilities.constantes import COMMERCIAL, SUPPORT, GESTION, SUPPORT_COLOR, GESTION_COLOR, RESET


class ShowEvenementsView(CommonView):
    controler = ShowEvenementsControler()

    def display_evenements(self, filtered=False):
        clear_screen()
        token = self.check_token_validity()

        if token is not False:
            if filtered is False:
                print("EVENEMENTS\n\n")
                evenements = get_all_evenements()
            elif filtered == "mes_evenements":
                print(SUPPORT_COLOR+"MES EVENEMENTS\n\n"+RESET)
                evenements = get_evenements_by_idSupport(token["id"])
            elif filtered == "evenements_sans_support":
                print(GESTION_COLOR+"AFFECTER UN SUPPORT A UN EVENEMENT\n\n"+RESET)
                evenements = get_evenements_without_support()

            ids_evenements = []
            for evenement in evenements:
                id = evenement.id
                ids_evenements.append(id)
                nom = evenement.nom
                print(f"{"║ "+str(id)[:5]:<5} | {nom[:40]:<40} ║")

            modificateur = -1    # pour choix action différencié
            if token["departement_id"] == COMMERCIAL:
                print("\n 1) Créer un événement")
                modificateur = 0
            if token["departement_id"] == SUPPORT:
                if ids_evenements.count() > 0:
                    print(" 1) Modifier un événement")
                    modificateur = 1
            if token["departement_id"] == GESTION:
                if ids_evenements.count() > 0:
                    print(" 1) Attribuer un événement")
                    modificateur = 2
            choix = input("\nEntrez le numéro d'une action \n"
                          "ou appuyez sur Entrée pour retourner au menu : ")
            # si action disponible et choisie
            if choix == "1" and modificateur > -1:
                if modificateur == 0:
                    choix = "1"
                    evenement = 0
                elif modificateur == 1:
                    evenement = input("Entrez l'id de l'événement à modifier: ")
                    int_evenement = int(evenement)
                    choix = "2"
                    if int_evenement not in ids_evenements:
                        print("id incorrect")
                        modificateur = 0
                        evenement = 0
                elif modificateur == 2:
                    evenement = input("Entrez l'id de l'événement à attribuer: ")
                    int_evenement = int(evenement)
                    if int_evenement not in ids_evenements:
                        print("id incorrect")
                        choix = "3"
                        evenement = 0
            else:
                choix = ""
                evenement = 0
            self.controler.select_action(choix, evenement)
        else:
            print("Session expirée")
