from utilities.clear_screen import clear_screen
from utilities.constantes import GESTION, GESTION_COLOR, RESET
from base_managing.CRUD import get_nom_departement_by_id
from views.common_view import CommonView
from controlers.show_single_collaborateur_controler import ShowSingleCollaborateursControler


class ShowSingleCollaborateurView(CommonView):
    controler = ShowSingleCollaborateursControler()

    def display_single_collaborateur(self, collaborateur):
        clear_screen()
        token = self.check_token_validity()
        if token is not False:
            print(GESTION_COLOR+"DONNEES COLLABORATEUR\n\n"+RESET)
            id = collaborateur.id
            login = collaborateur.login
            email = collaborateur.email
            nom_departement = get_nom_departement_by_id(collaborateur.departement_id)
            print(" id: "+str(id))
            print(" 1) login:       "+login)
            print(" 2) mot de passe: ****")
            print(" 3) email:       "+email)
            print(" 4) id / nom département: "+str(collaborateur.departement_id)+" / "+nom_departement)
            if token["departement_id"] == GESTION:
                self.controler.idCollaborateur = id
                print("Appuyez sur entrée pour retourner à l'écran précédent")
                print("ou entrez le numéro d'élément à modifier")
                action = int(input("Votre choix: "))
            else:
                input("Appuyez sur entrée pour retourner à l'écran précédent")
                action = ""
            self.controler.check_action(action, id)
        else:
            print("Session expirée")

    def display_update(self, field_number):
        print("\n")
        match field_number:
            case 1:
                new_login = input("nouveau login: ")
                return "login", new_login
            case 2:
                new_password = input("nouveau mot de passe: ")
                return "password", new_password
            case 3:
                new_email = input("nouvel email: ")
                return "email", new_email
            case 4:
                new_departement_id = int(input("nouvel id departement: "))
                return "departement_id", new_departement_id

        if self.controler.check_token_validity() is not False:
            self.controler.save_new_value()
