from views.common_view import CommonView
from controlers.create_evenement_controler import CreateEvenementControler
from utilities.clear_screen import clear_screen
from utilities.constantes import COMMERCIAL_COLOR, RESET
from base_managing.CRUD import get_client_by_id, get_contrat_by_id


class CreateEvenementView(CommonView):
    """
    View to manage the creation of an 'evenement'

    Use the controler `CreateEvenementControler` to
    manage user's inputs
    """

    controler = CreateEvenementControler()

    def input_datas(self):
        """
        Manage the input of datas for the creation
        of an 'evenement' and save the new 'evenement'
        """
        clear_screen()
        print(COMMERCIAL_COLOR+"NOUVEL EVENEMENT\n\n"+RESET)

        nom = input("Nom de l'événement: ")
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
        lieu = input("lieu de l'évenement: ")
        adresse = input("adresse du lieu: ")
        participants = int(input("nombre de participants: "))
        date_debut = input("date début, format AAAA-MM-JJ HH:MM:SS: ")
        date_fin = input("date fin, format AAAA-MM-JJ HH:MM:SS: ")

        datas = [nom, client_id, contrat_id, lieu, adresse, participants, date_debut, date_fin]
        self.controler.save_new_evenement(datas)
