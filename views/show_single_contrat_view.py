from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import GESTION, COMMERCIAL, CYAN, RESET


class ShowSingleContratView(CommonView):
    color = CYAN

    def display_single_contrat(self, idContrat):
        clear_screen()
        token = self.check_token_validity()
        if token is not False:
            print(self.color+"DONNEES CONTRAT\n\n"+RESET)
