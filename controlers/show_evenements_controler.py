from base_managing.CRUD import get_evenement_by_id, update_evenement, delete_evenement
from controlers.common_controler import CommonControler
from views.show_single_evenement_view import ShowSingleEvenementView
from views.create_evenement_view import CreateEvenementView


class ShowEvenementsControler(CommonControler):
    """
    Controler for the view ShowEvenementsView

    Used to manage user's actions
    """

    def select_action(self, choix, evenement):
        """
        Manage the action defined in the view

        Args:
            choix (string): number of the action
            evenement (string): id of an 'evenement'
        """
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if choix in ["1", "2", "3", "4", "5"]:
                if choix == "1":
                    evenement = int(evenement)
                    # selection d'une fiche evenement
                    evenement = get_evenement_by_id(evenement)
                    if evenement is not False:
                        view = ShowSingleEvenementView()
                        view.display_single_evenement(evenement)
                    else:
                        print("id incorrect !")
                if choix == "2":
                    view = CreateEvenementView()
                    view.input_datas()
                if choix == "3":  # modification
                    # selection d'une fiche evenement
                    evenement = get_evenement_by_id(evenement)
                    if evenement is not False:
                        view = ShowSingleEvenementView()
                        view.display_single_evenement(evenement, True)
                    else:
                        print("id incorrect !")
                if choix == "4":
                    # selection d'une fiche evenement
                    evenement = get_evenement_by_id(evenement)
                    if evenement is not False:
                        view = ShowSingleEvenementView()
                        view.display_single_evenement(evenement, True)
                    else:
                        print("id incorrect !")
                if choix == "5":
                    delete_evenement(evenement)
                    from views.show_evenements_view import ShowEvenementsView
                    view = ShowEvenementsView()
                    view.display_evenements()
            else:
                # retour au menu
                from views.main_menu_view import MainMenuView
                view = MainMenuView()
                view.display_items()
        else:
            print("Session expirée")

    def attribute_support_evenenement(self, idEvenement, idSupport):
        """
        Assigne a support collaborator to an 'evenement'

        Args:
            idEvenement (int): id of the 'evenement'
            idSupport (int): id of the support collaborator to assign
        """
        update_evenement(idEvenement, "responsable_support_id", idSupport)
