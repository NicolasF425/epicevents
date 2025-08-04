from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import COMMERCIAL, GESTION_COLOR, RESET
from base_managing.CRUD import get_client_by_id, get_collaborateur_by_id


class CreateContratView(CommonView):

    def input_datas():
        clear_screen()
        print(GESTION_COLOR+"NOUVEAU CONTRAT\n\n"+RESET)

        client_id = input("Id du client: ")
        commercial_id = input("Id du commercial: ")
        montant_total = input("Montant total: ")
        montant_restant = input("Montant restant: ")

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
                id_commercial = int(input("identifiant du commercial: "))
                result = get_collaborateur_by_id(id_commercial)
                if result is not False:
                    if result.departement_id == COMMERCIAL:
                        OK = True
                    else:
                        print("Veillez entrez l'identifiant d'un commercial\n")
                else:
                    print("identifiant non trouvé\n")
            except ValueError:
                print("Veuillez entrer une valeur numérique")

            datas = [client_id, commercial_id, montant_total, montant_restant]
            return datas
