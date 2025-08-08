from views.common_view import CommonView
from utilities.clear_screen import clear_screen


class ShowSingleEvenementView(CommonView):

    def display_single_evenement(self, evenement):
        clear_screen()
        token = self.check_token_validity()
        if token is not False:
            print("DONNEES EVENEMENT\n\n")
            print("id: "+str(evenement.id))
            print("nom: "+evenement.nom)
            print("id client: "+evenement.client_id)
            print("id contrat: "+evenement.contrat_id)
