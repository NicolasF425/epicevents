from views.common_view import CommonView
from controlers.show_single_client_controler import ShowSingleClientControler
from utilities.clear_screen import clear_screen
from utilities.constantes import COMMERCIAL, COMMERCIAL_COLOR, RESET


class ShowSingleClientView(CommonView):
    '''
    View to display and mofification of a single "client"

    Use the controler `ShowSingleClientControler` to
    manage user's actions
    '''
    controler = ShowSingleClientControler()

    def display_single_client(self, client):
        """
        Display fields and values for a single 'client'

        Args:
            evenement : a 'client' object
            update (bool, optional): if the update is doable. Defaults to False.
        """
        clear_screen()
        token = self.check_token_validity()
        if token is not False:
            print(COMMERCIAL_COLOR+"DONNEES CLIENT\n\n"+RESET)
            id = client.id
            nom_complet = client.nom_complet
            email = client.email
            telephone = client.telephone
            entreprise = client.nom_entreprise

            print(" id: "+str(id)+"\n")
            print(" 1) nom complet:       "+nom_complet)
            print(" 2) email:             "+email)
            print(" 3) téléphone:         "+telephone)
            print(" 4) entreprise:        "+entreprise)

            if token["departement_id"] == COMMERCIAL:
                print("\nAppuyez sur entrée pour retourner à l'écran précédent")
                print("ou entrez le numéro d'élément à modifier")
                action = input("Votre choix: ")
            else:
                input("\nAppuyez sur entrée pour retourner à l'écran précédent")
                action = ""
            self.controler.check_action(action, id)
        else:
            print("Session expirée")

    def display_update(self, idClient, field_number):
        """
        Display the field selected and input the new value
        Save the updated 'client'

        Args:
            field_number (string): the number in the field list
            id (int): the id of the 'client' to update
        """
        print("\n")
        match field_number:
            case 1:
                new_nom = input("nouveau nom: ")
                datas = ["nom_complet", new_nom]
            case 2:
                new_email = input("nouvel email: ")
                datas = ["email", new_email]
            case 3:
                new_telephone = input("nouveau numéro de téléphone: ")
                datas = ["telephone", new_telephone]
            case 4:
                new_nom_entreprise = input("nouveau nom d'entreprise: ")
                datas = ["nom_entreprise", new_nom_entreprise]

        if self.controler.check_token_validity() is not False:
            self.controler.save_new_value(idClient, datas[0], datas[1])
