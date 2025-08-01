from base_managing.CRUD import get_all_contrats, get_client_by_id
from views.common_view import CommonView
from utilities.clear_screen import clear_screen


class ShowContratsView(CommonView):

    def display_contrats(self):
        clear_screen()
        token = self.check_token_validity()

        if token is not False:
            print("CONTRATS\n\n")
            contrats = get_all_contrats()
            for contrat in contrats:
                id = contrat.id
                client = contrat.client_id
                nom_client = get_client_by_id(client).nom_entreprise
                print(f"{"║ "+str(id)[:5]:<5} | {nom_client[:30]:<30} ║")
            input("")
        else:
            print("Session expirée")
