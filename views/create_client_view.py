from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from utilities.constantes import COMMERCIAL, COMMERCIAL_COLOR, RESET
from base_managing.CRUD import get_collaborateur_by_id


class CreateClientView(CommonView):

    def input_datas():
        clear_screen()
        print(COMMERCIAL_COLOR+"NOUVEAU CLIENT\n\n"+RESET)

        nom_complet = input("nom complet: ")
        email = input("email: ")
        telephone = input("téléphone: ")
        entreprise = input("entreprise: ")
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

            datas = [nom_complet, email, telephone, entreprise, commercial_id]
            return datas
