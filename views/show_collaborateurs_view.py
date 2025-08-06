from base_managing.CRUD import get_all_collaborateurs, get_nom_departement_by_id
from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import GESTION_COLOR, RESET
from controlers.show_collaborateurs_controler import ShowCollaborateursControler


class ShowCollaborateursView(CommonView):
    controler = ShowCollaborateursControler()

    def display_collaborateurs(self):
        clear_screen()
        token = self.check_token_validity()

        if token is not False:
            print(GESTION_COLOR+"COLLABORATEURS\n\n"+RESET)
            collaborateurs = get_all_collaborateurs()
            print(f"{"║ id"[:5]:<5} | {"login"[:25]:<25} | {"email"[:25]:<25} | {"departement"[:20]:<20}"+"║\n")

            for collaborateur in collaborateurs:
                id = collaborateur.id
                login = collaborateur.login
                email = collaborateur.email
                nom_departement = get_nom_departement_by_id(collaborateur.departement_id)

                print(f"{"║ "+str(id)[:5]:<5} | {login[:25]:<25} | {email[:25]:<25} | {nom_departement[:20]:<20}║")
            print("\n 1) Créer un nouveau collaborateur")
            print(" 2) Modifier un collaborateur")
            print(" 3) Supprimer un collaborateur")
            choix = input("\nEntrez le numéro d'une action "
                          "ou appuyez sur Entrée pour retourner au menu : ")
            if choix == "1":
                collaborateur = 0
            elif choix == "2":
                collaborateur = input("Entrez l'id du collaborateur à modifier: ")
            elif choix == "3":
                collaborateur = input("Entrez l'id du collaborateur à supprimer: ")
            else:
                choix = ""
                collaborateur = 0
            self.controler.select_action(choix, collaborateur)
        else:
            print("Session expirée")
