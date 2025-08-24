from views.common_view import CommonView
from controlers.show_single_contrat_controler import ShowSingleContratControler
from utilities.clear_screen import clear_screen
from utilities.constantes import CYAN, RESET


class ShowSingleContratView(CommonView):
    '''
    View to display and mofification of a single "contrat"

    Use the controler `ShowSingleContratsControler` to
    manage user's actions
    '''
    controler = ShowSingleContratControler()

    def display_single_contrat(self, contrat, update=False):
        """
        Display fields and values for a single 'contrat'

        Args:
            evenement : a 'contrat' object
            update (bool, optional): if the update is doable. Defaults to False.
        """
        clear_screen()
        token = self.check_token_validity()
        if token is not False:
            print(CYAN+"DONNEES CONTRAT\n\n"+RESET)
            id = contrat.id
            client_id = contrat.client_id
            commercial_id = contrat.commercial_id
            montant_total = contrat.montant_total
            montant_restant = contrat.montant_restant
            date_creation = contrat.date_creation
            statut_contrat = contrat.est_signe

            print(" id: "+str(id))
            print("\n id client: "+str(client_id))
            print(" 1) id commercial: "+str(commercial_id))
            print(" 2) montant total: "+str(montant_total))
            print(" 3) montant restant: "+str(montant_restant))
            print(f" date création: {date_creation.strftime('%d/%m/%Y %H:%M:%S')}")
            est_signe = "non"
            if statut_contrat:
                est_signe = "oui"
            print(" 4) contrat signé: "+est_signe)
            if not update:
                action = input("\nAppuyez sur Entrée pour revenir au menu: ")
                action = ""
            else:
                action = input("\nEntrez le numéro de l'élément à "
                               "modifier ou appuyez sur Entrée pour revenir au menu: ")
            self.controler.check_action(action, id)

    def display_update(self, field_number, id):
        """
        Display the field selected and input the new value
        Save the updated 'contrat'

        Args:
            field_number (string): the number in the field list
            id (int): the id of the 'contrat' to update
        """
        print("\n")
        infos = []
        match field_number:
            case "1":
                new_commercial_id = input("id du nouveau commercial associé : ")
                infos = ["commercial_id", new_commercial_id]
            case "2":
                new_montant_total = input("nouveau montant total: ")
                infos = ["montant_total", new_montant_total]
            case "3":
                new_montant_restant = input("nouveau montant restant: ")
                infos = ["montant_restant", new_montant_restant]
            case "4":
                new_est_signe = int(input("nouveau statut (0=non signé, 1=signé): "))
                new_est_signe = bool(int(new_est_signe))
                infos = ["est_signe", new_est_signe]

        if self.controler.check_token_validity() is not False:
            if infos:
                self.controler.save_new_value(id, infos[0], infos[1])
