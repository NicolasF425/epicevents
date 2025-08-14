from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from controlers.show_single_evenement_controler import ShowSingleEvenementControler
from base_managing.CRUD import get_collaborateurs_by_idDepartement
from utilities.constantes import SUPPORT, GESTION


class ShowSingleEvenementView(CommonView):
    controler = ShowSingleEvenementControler()

    def display_single_evenement(self, evenement, update=False):
        clear_screen()
        token = self.check_token_validity()

        if token is not False:
            if token['departement_id'] == SUPPORT and update:
                idSupport = 0
                print("DONNEES EVENEMENT\n\n")
                print(" 1) id: "+str(evenement.id))
                print(" 2) nom: "+evenement.nom)
                print(" 3) id client: "+str(evenement.client_id))
                print(" 4) id contrat: "+str(evenement.contrat_id))
                element = input("\nEntrez le numéro de l'élément à "
                                "modifier ou appyez sur Entrée pour revenir au menu: ")
            elif token['departement_id'] == GESTION and update:
                element = 0
                collaborateurs = get_collaborateurs_by_idDepartement(SUPPORT)
                print(f"{"║ id"[:5]:<5} | {"login"[:25]:<25} | {"email"[:25]:<25} ║\n")
                ids_collaborateurs = []
                for collaborateur in collaborateurs:
                    id = collaborateur.id
                    ids_collaborateurs.append(id)
                    login = collaborateur.login
                    email = collaborateur.email
                    print(f"{"║ "+str(id)[:5]:<5} | {login[:25]:<25} | {email[:25]:<25} ║")
                print("\nEntrez le numéro de collaborateur support à affecter")
                inputIdSupport = input("ou appuyez sur Entrée pour revenir au menu: ")
                if inputIdSupport != "":
                    idSupport = int(inputIdSupport)
            else:
                print("DONNEES EVENEMENT\n\n")
                print(" id: "+str(evenement.id))
                print(" nom: "+evenement.nom)
                print(" id client: "+str(evenement.client_id))
                print(" id contrat: "+str(evenement.contrat_id))
                input("\n Appuyez sur Entrée pour revenir au menu: ")
                element = ""
                idSupport = 0

            self.controler.check_action(element, evenement.id, idSupport, token['departement_id'])

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
