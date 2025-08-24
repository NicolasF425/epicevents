from utilities.clear_screen import clear_screen
from utilities.constantes import GESTION, GESTION_COLOR, RESET
from base_managing.CRUD import get_nom_departement_by_id
from views.common_view import CommonView
from controlers.show_single_collaborateur_controler import ShowSingleCollaborateursControler


class ShowSingleCollaborateurView(CommonView):
    '''
    View to display and mofification of a single "collaborateur"

    Use the controler `ShowSingleCollaborateurControler` to
    manage user's actions
    '''
    controler = ShowSingleCollaborateursControler()

    def display_single_collaborateur(self, collaborateur):
        """
        Display fields and values for a single 'collaborateur'

        Args:
            evenement : a 'collaborateur' object
            update (bool, optional): if the update is doable. Defaults to False.
        """
        clear_screen()
        token = self.check_token_validity()
        if token is not False:
            print(GESTION_COLOR+"DONNEES COLLABORATEUR\n\n"+RESET)
            id = collaborateur.id
            login = collaborateur.login
            email = collaborateur.email
            nom_departement = get_nom_departement_by_id(collaborateur.departement_id)
            print(" id: "+str(id))
            print("\n 1) login:       "+login)
            print(" 2) mot de passe: ****")
            print(" 3) email:       "+email)
            print(" 4) id / nom département: "+str(collaborateur.departement_id)+" / "+nom_departement)

            if token["departement_id"] == GESTION:
                self.controler.idCollaborateur = id
                print("\nAppuyez sur entrée pour retourner à l'écran précédent")
                action = int(input("ou entrez le numéro d'élément à modifier: "))
            else:
                input("\nAppuyez sur entrée pour retourner à l'écran précédent")
                action = ""
            self.controler.check_action(action, id)
        else:
            print("Session expirée")

    def display_update(self, field_number, id):
        """
        Display the field selected and input the new value
        Save the updated 'collaborateur'

        Args:
            field_number (string): the number in the field list
            id (int): the id of the 'collaborateur' to update
        """
        print("\n")
        infos = []
        match field_number:
            case 1:
                new_login = input("nouveau login: ")
                infos = ["login", new_login]
            case 2:
                new_password = input("nouveau mot de passe: ")
                infos = ["password", new_password]
            case 3:
                new_email = input("nouvel email: ")
                infos = ["email", new_email]
            case 4:
                new_departement_id = int(input("nouvel id departement: "))
                infos = ["departement_id", new_departement_id]

        if self.controler.check_token_validity() is not False:
            if infos:
                self.controler.save_new_value(id, infos[0], infos[1])
        else:
            print("Session expirée")
