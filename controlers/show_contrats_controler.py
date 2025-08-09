from base_managing.CRUD import get_contrat_by_id, delete_contrat
from controlers.common_controler import CommonControler
from views.show_single_contrat_view import ShowSingleContratView
from views.create_contrat_view import CreateContratView
from utilities.pause import pause


class ShowcontratsControler(CommonControler):

    def select_action(self, choix, contrat):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if choix in ["1", "2", "3"]:
                if choix == "1":
                    view = CreateContratView()
                    view.input_datas()
                if choix == "2":  # modification
                    try:
                        contrat = int(contrat)
                        # selection d'une fiche contrat
                        contrat = get_contrat_by_id(contrat)
                        if contrat is not False:
                            view = ShowSingleContratView()
                            view.display_single_contrat(contrat)
                        else:
                            print("id incorrect !")
                    except ValueError:
                        # si ce n'est pas un nombre
                        print("Entrez un nombre")
                if choix == "3":
                    try:
                        contrat = int(contrat)
                    except ValueError:
                        # si ce n'est pas un nombre
                        print("Entrez un nombre")
                    try:
                        if type(contrat) is int:
                            delete_contrat(contrat)
                            print("contrat supprimé")
                            pause(3)
                            from views.show_contrats_view import ShowContratsView
                            view = ShowContratsView()
                            view.display_contrats()
                    except ValueError:
                        print("id incorrect !")
            elif choix in ["4", "5", "6"]:
                filtres = ["mes contrats", "non signe", "non totalement paye"]
                from views.show_contrats_view import ShowContratsView
                view = ShowContratsView()
                view.filter = filtres[int(choix)-4]
                view.display_contrats()
            else:
                # retour au menu
                from views.main_menu_view import MainMenuView
                view = MainMenuView()
                view.display_items()
        else:
            print("Session expirée")
