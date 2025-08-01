from base_managing.CRUD import get_all_evenements
from views.common_view import CommonView
from utilities.clear_screen import clear_screen


class ShowEvenementsView(CommonView):

    def display_evenements(self):
        clear_screen()
        token = self.check_token_validity()

        if token is not False:
            print("EVENEMENTS\n\n")
            evenements = get_all_evenements()
            for evenement in evenements:
                id = evenement.id
                nom = evenement.nom
                print(f"{"║ "+str(id)[:5]:<5} | {nom[:40]:<40} ║")
            input("")
        else:
            print("Session expirée")
