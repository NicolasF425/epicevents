from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import COMMERCIAL, GESTION_COLOR, RESET
from base_managing.CRUD import get_client_by_id, get_collaborateur_by_id
from controlers.create_contrat_controler import CreateContratControler


class CreateContratView(CommonView):
    controler = CreateContratControler()

    def input_datas(self):
        token = self.check_token_validity()

        if token is not False:
            clear_screen()
            print(GESTION_COLOR+"NOUVEAU CONTRAT\n\n"+RESET)

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
                    commercial_id = int(input("identifiant du commercial: "))
                    result = get_collaborateur_by_id(commercial_id)
                    if result is not False:
                        if result.departement_id == COMMERCIAL:
                            OK = True
                        else:
                            print("Veillez entrez l'identifiant d'un commercial\n")
                    else:
                        print("identifiant non trouvé\n")
                except ValueError:
                    print("Veuillez entrer une valeur numérique")

            montant_total = float(input("Montant total: "))
            montant_restant = float(input("Montant restant: "))
            est_signe = input("contrat signé, 1=oui, 0=non: ")
            try:
                est_signe = bool(int(est_signe))
            except ValueError:
                print("Valeur différente de 0 ou 1")
            datas = [client_id, commercial_id, montant_total, montant_restant, est_signe]
            self.controler.save_new_contrat(datas)
        else:
            print("session expirée")
