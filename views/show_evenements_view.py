from base_managing.CRUD import get_all_evenements, get_evenements_by_idSupport, get_evenements_without_support
from base_managing.CRUD import get_collaborateurs_by_idDepartement
from views.common_view import CommonView
from controlers.show_evenements_controler import ShowEvenementsControler
from utilities.clear_screen import clear_screen
from utilities.constantes import COMMERCIAL, SUPPORT, GESTION, SUPPORT_COLOR, GESTION_COLOR, COMMERCIAL_COLOR, RESET


class ShowEvenementsView(CommonView):
    """
    View to display of a list of 'evenement'

    Use the controler `ShowEvenementsControler` to
    manage user's actions
    """
    controler = ShowEvenementsControler()

    def display_evenements(self, filtered=False):
        """
        Display a list of 'client' and input for an action

        Args:
            filtered (bool, optional): if a filter should be applied . Defaults to False.
        """
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
            print(f"{"║ "+"id"[:5]:<5} | {"nom"[:40]:<40} ║\n")
            for evenement in evenements:
                id = evenement.id
                ids_evenements.append(id)
                nom = evenement.nom
                print(f"{"║ "+str(id)[:5]:<5} | {nom[:40]:<40} ║")

            modificateur = -1    # pour differencier choix action
            print("\n 1) Voir les détails d'un événement")
            if token["departement_id"] == COMMERCIAL:
                print(COMMERCIAL_COLOR+" 2) Créer un événement"+RESET)
                modificateur = 0
            if token["departement_id"] == SUPPORT:
                if len(ids_evenements) > 0:
                    print(" 2) Modifier un événement")
                    modificateur = 1
            if token["departement_id"] == GESTION:
                if len(ids_evenements) > 0:
                    print(" 2) Attribuer un événement")
                    modificateur = 2
            if token["departement_id"] == COMMERCIAL:
                if len(ids_evenements) > 0:
                    print(COMMERCIAL_COLOR+" 3) Supprimer un événement"+RESET)
                    modificateur = 3
            choix = input("\nEntrez le numéro d'une action \n"
                          "ou appuyez sur Entrée pour retourner au menu : ")
            # si action disponible et choisie
            if choix == "1":
                evenement = input("Entrez l'id de l'événement à modifier: ")
                evenement = int(evenement)
            elif choix == "2" and modificateur > -1:
                if modificateur == 0:   # Creation evenement
                    choix = "2"
                    evenement = 0
                elif modificateur == 1:
                    evenement = input("Entrez l'id de l'événement à modifier: ")
                    evenement = int(evenement)
                    choix = "3"
                    if evenement not in ids_evenements:
                        print("id incorrect")
                        choix = ""
                        evenement = 0
                elif modificateur == 2:
                    evenement = input("Entrez l'id de l'événement à attribuer: ")
                    evenement = int(evenement)
                    choix = "4"
                    if evenement not in ids_evenements:
                        print("id incorrect")
                        choix = ""
                        evenement = 0
            elif choix == "3" and modificateur == 3:
                evenement = input("Entrez l'id de l'événement à supprimer: ")
                evenement = int(evenement)
                choix = "5"
                if evenement not in ids_evenements:
                    print("id incorrect")
                    choix = ""
                    evenement = 0
            else:
                choix = ""
                evenement = 0
            self.controler.select_action(choix, evenement)
        else:
            print("Session expirée")

    def attribute_support_evenement(self, idEvenement):
        """
        Display and manage the attribution
        of a support department collaborator to an "evenement".
        """
        collaborateurs = get_collaborateurs_by_idDepartement(SUPPORT)
        ids = []
        print("\n")
        if collaborateurs:
            print(f"{"║ "+"id"[:5]:<5} | {"login"[:25]:<25} | {"email"[:25]:<25} ║\n\n")
            for collaborateur in collaborateurs:
                id = collaborateur.id
                ids.append(id)
                login = collaborateur.login
                email = collaborateur.email
                print(f"{"║ "+str(id)[:5]:<5} | {login[:25]:<25} | {email[:25]:<25} ║")
            print("\n")
        idSupport = input("Entrez l'id du collaborateur à affecter: ")
        if idSupport in ids:
            idSupport = int(idSupport)
            self.controler.attribute_support_evenenement(idEvenement, idSupport)
        else:
            print("id non trouvé")
