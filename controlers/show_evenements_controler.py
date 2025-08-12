from base_managing.CRUD import get_evenement_by_id, delete_evenement
from controlers.common_controler import CommonControler
from views.show_single_evenement_view import ShowSingleEvenementView
from views.create_evenement_view import CreateEvenementView
from utilities.pause import pause


class ShowEvenementsControler(CommonControler):

    def select_action(self, choix, evenement):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if choix in ["1", "2", "3"]:
                if choix == "1":
                    view = CreateEvenementView()
                    view.input_datas()
                if choix == "2":  # modification
                    evenement = int(evenement)
                    # selection d'une fiche evenement
                    evenement = get_evenement_by_id(evenement)
                    if evenement is not False:
                        view = ShowSingleEvenementView()
                        view.display_single_evenement(evenement)
                    else:
                        print("id incorrect !")
                if choix == "3":
                    try:
                        evenement = int(evenement)
                    except ValueError:
                        # si ce n'est pas un nombre
                        print("Entrez un nombre")
                    try:
                        if type(evenement) is int:
                            delete_evenement(evenement)
                            print("evenement supprimé")
                            pause(3)
                            from views.show_evenements_view import ShowEvenementsView
                            view = ShowEvenementsView()
                            view.display_evenements()
                    except ValueError:
                        print("id incorrect !")
            else:
                # retour au menu
                from views.main_menu_view import MainMenuView
                view = MainMenuView()
                view.display_items()
        else:
            print("Session expirée")
