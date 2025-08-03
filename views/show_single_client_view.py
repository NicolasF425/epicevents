from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import COMMERCIAL, BLUE, RESET


class ShowSingleClientView(CommonView):
    color = BLUE

    def display_single_client(self, idClient):
        clear_screen()
        token = self.check_token_validity()
        if token is not False:
            print(self.color+"DONNEES CLIENT\n\n"+RESET)
            input("")
