from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import GESTION, COMMERCIAL, CYAN, RESET


class ShowSingleContratView(CommonView):

    def display_single_contrat(self, contrat):
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
            statut_contrat = contrat.statut

            print(" id: "+str(id))
            print(" id / nom client:"+str(client_id)+" / ")
            print(" 1) id / commercial: "+str(commercial_id)+" / ")
            print(" 2) montant total: "+str(montant_total)+" / ")
            print(" 3) montant restant: "+str(montant_restant)+" / ")
            print(" date création: "+date_creation)
            print(" statut contrat"+statut_contrat)


    def display_update(self, field_number):
        print("\n")
        match field_number:
            case 1:
                pass