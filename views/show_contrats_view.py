from base_managing.CRUD import get_all_contrats
from views.common_view import CommonView
from utilities.clear_screen import clear_screen


class ShowContratsView(CommonView):

    def display_contrats(self):
        contrats = get_all_contrats()

        clear_screen()

        for contrat in contrats:
            id = contrat.id
            client = contrat.client
            print(str(id)+" "+client)
