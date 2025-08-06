from views.common_view import CommonView
from controlers.show_single_contrat_controler import ShowSingleContratControler
from utilities.clear_screen import clear_screen
from utilities.constantes import CYAN, RESET


class ShowSingleContratView(CommonView):
    controler = ShowSingleContratControler()

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
            statut_contrat = contrat.est_signe

            print(" id: "+str(id))
            print(" id / nom client:"+str(client_id)+" / ")
            print(" 1) id / commercial: "+str(commercial_id)+" / ")
            print(" 2) montant total: "+str(montant_total)+" / ")
            print(" 3) montant restant: "+str(montant_restant)+" / ")
            print(" date création: "+date_creation)
            print(" 4) contrat signé: "+statut_contrat)

    def display_update(self, field_number):
        print("\n")
        match field_number:
            case 1:
                new_commercial_id = input("id du nouveau commercial associé : ")
                return "commercial_id", new_commercial_id
            case 2:
                new_montant_total = input("nouveau montant total: ")
                return "montant_total", new_montant_total
            case 3:
                new_montant_restant = input("nouveau montant restant: ")
                return "email", new_montant_restant
            case 4:
                new_est_signe = int(input("nouveau statut (0=non signé, 1=signé): "))
                return "departement_id", new_est_signe

        if self.controler.check_token_validity() is not False:
            self.controler.save_new_value()
