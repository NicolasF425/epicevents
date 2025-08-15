from base_managing.CRUD import get_contrat_by_id
from controlers.common_controler import CommonControler
from views.show_single_contrat_view import ShowSingleContratView
from views.create_contrat_view import CreateContratView
from utilities.constantes import COMMERCIAL, GESTION


class ShowcontratsControler(CommonControler):

    def select_action(self, choix, contrat, update=False):
        token = self.check_token_validity()

        if token is not False:
            if choix in ["1", "2"]:
                if choix == "1" and token['departement_id'] == GESTION:    # creation
                    view = CreateContratView()
                    view.input_datas()
                elif (choix == "1" and token['departement_id'] == COMMERCIAL) or \
                     (choix == "2" and token['departement_id'] == GESTION):  # modification
                    try:
                        contrat = int(contrat)
                        # selection d'une fiche contrat
                        contrat = get_contrat_by_id(contrat)
                        if contrat is not False:
                            view = ShowSingleContratView()
                            view.display_single_contrat(contrat, update=True)
                        else:
                            print("id incorrect !")
                    except ValueError:
                        # si ce n'est pas un nombre
                        print("Entrez un nombre")
                else:
                    try:
                        contrat = int(contrat)
                        # selection d'une fiche contrat
                        contrat = get_contrat_by_id(contrat)
                        if contrat is not False:
                            view = ShowSingleContratView()
                            view.display_single_contrat(contrat, update)
                        else:
                            print("id incorrect !")
                    except ValueError:
                        # si ce n'est pas un nombre
                        print("Entrez un nombre")
            elif choix in ["2", "3", "4"] and token['departement_id'] == COMMERCIAL:
                filtres = ["mes contrats", "non signe", "non totalement paye"]
                from views.show_contrats_view import ShowContratsView
                view = ShowContratsView()
                view.filter = filtres[int(choix)-3]
                view.display_contrats()
            else:
                # retour au menu
                from views.main_menu_view import MainMenuView
                view = MainMenuView()
                view.display_items()
        else:
            print("Session expirée")
