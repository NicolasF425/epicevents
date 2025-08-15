from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import COMMERCIAL_COLOR, RESET
from base_managing.CRUD import get_client_by_id, get_contrat_by_id


class CreateEvenementView(CommonView):

    def input_datas(self):
        clear_screen()
        print(COMMERCIAL_COLOR+"NOUVEL EVENEMENT\n\n"+RESET)

        nom = input("Nom de l'événement: ")
        client_id = input("Id du client")
        contrat_id = input("Id du contrat: ")
        support_id = None
        OK = False
        while not OK:
            try:
                client_id = int(input("identifiant du client: "))
                result = get_client_by_id(client_id)
                if result is not False:
                    OK = True
                else:
                    print("identifiant non trouvé\n")
            except ValueError:
                print("Veuillez entrer une valeur numérique")

        OK = False
        while not OK:
            try:
                contrat_id = int(input("identifiant du contrat: "))
                result = get_contrat_by_id(contrat_id)
                if result is not False:
                    OK = True
                else:
                    print("identifiant non trouvé\n")
            except ValueError:
                print("Veuillez entrer une valeur numérique")

            datas = [nom, client_id, support_id]
            return datas
