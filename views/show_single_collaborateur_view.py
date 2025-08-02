from utilities.clear_screen import clear_screen
from utilities.constantes import GESTION, RED, RESET
from base_managing.CRUD import get_nom_departement_by_id
from views.common_view import CommonView
from controlers.show_single_collaborateur_controler import ShowSingleCollaborateursControler


class ShowSingleCollaborateurView(CommonView):
    controler = ShowSingleCollaborateursControler()
    color = RED

    def display_single_collaborateur(self, collaborateur):
        clear_screen()
        token = self.check_token_validity()
        if token is not False:
            print(self.color+"DONNEES COLLABORATEUR\n\n"+RESET)
            id = collaborateur.id
            login = collaborateur.login
            email = collaborateur.email
            nom_departement = get_nom_departement_by_id(collaborateur.departement_id)
            print("    id:          "+str(id))
            print(" 1) login:       "+login)
            print(" 2) mot de passe: ****")
            print(" 3) email:       "+email)
            print(" 4) département: "+nom_departement+" / "+str(collaborateur.departement_id))
            print("Appuyez sur entrée pour retourner à l'écran précédent")
            if token["departement_id"] == GESTION:
                print("Ou entrez le numéro d'élément à modifier")
                action = input("Votre choix: ")
            else:
                action = input("Votre choix: ")
                action = ""
            self.controler.select_action(action)
        else:
            print("Session expirée")
