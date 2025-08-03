from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import GESTION, SUPPORT, BLUE, RESET


class ShowSingleEvenementView(CommonView):
    color = BLUE

    def display_single_evenement(self, idEvenement):
        clear_screen()
        token = self.check_token_validity()
        if token is not False:
            print(self.color+"DONNEES EVENEMENT\n\n"+RESET)
