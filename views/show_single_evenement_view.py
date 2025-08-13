from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from controlers.show_single_evenement_controler import ShowSingleEvenementControler


class ShowSingleEvenementView(CommonView):
    controler = ShowSingleEvenementControler()

    def display_single_evenement(self, evenement):
        clear_screen()
        token = self.check_token_validity()
        if token is not False:
            print("DONNEES EVENEMENT\n\n")
            print("id: "+str(evenement.id))
            print("nom: "+evenement.nom)
            print("id client: "+evenement.client_id)
            print("id contrat: "+evenement.contrat_id)

            action = input("\nEntrez le numéro de l'élément à "
                           "modifier ou appyez sur Entrée pour revenir au menu: ")
            self.controler.check_action(action, id)

    def display_update(self, field_number, id):
        print("\n")
        infos = []
        match field_number:
            case 1:
                new_nom = input("nouveau nom: ")
                infos = ["nom", new_nom]

        if self.controler.check_token_validity() is not False:
            if infos:
                self.controler.save_new_value(id, infos[0], infos[1])
