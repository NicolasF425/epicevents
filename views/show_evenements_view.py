from base_managing.CRUD import get_all_evenements
from views.common_view import CommonView
from utilities.clear_screen import clear_screen


class ShowEvenementsView(CommonView):

    def display_evenements(self):
        evenements = get_all_evenements()

        clear_screen()

        for evenement in evenements:
            id = evenement.id
            nom = evenement.nom
            print(str(id)+" "+nom)
