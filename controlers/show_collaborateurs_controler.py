from base_managing.CRUD import get_collaborateur_by_id, delete_collaborateur
from controlers.common_controler import CommonControler
from views.show_single_collaborateur_view import ShowSingleCollaborateurView
from views.create_collaborateur_view import CreateCollaborateurView


class ShowCollaborateursControler(CommonControler):
    """
    Controler for the view ShowCollaborateursView

    Used to manage user's actions
    """

    def select_action(self, choix, collaborateur):
        """
        Manage the action defined in the view

        Args:
            choix (string): number of the action
            collaborateur (string): id of a 'collaborateur
        """
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if choix in ["1", "2", "3"]:
                if choix == "1":
                    view = CreateCollaborateurView()
                    view.input_datas()
                if choix == "2":  # modification
                    try:
                        collaborateur = int(collaborateur)
                        # selection d'une fiche collaborateur
                        collaborateur = get_collaborateur_by_id(collaborateur)
                        if collaborateur is not False:
                            view = ShowSingleCollaborateurView()
                            view.display_single_collaborateur(collaborateur)
                        else:
                            print("id incorrect !")
                    except ValueError:
                        # si ce n'est pas un nombre
                        print("Entrez un nombre")
                if choix == "3":
                    delete_collaborateur(collaborateur)
                    print("collaborateur supprimé")
                    from views.show_collaborateurs_view import ShowCollaborateursView
                    view = ShowCollaborateursView()
                    view.display_collaborateurs()
            else:
                # retour au menu
                from views.main_menu_view import MainMenuView
                view = MainMenuView()
                view.display_items()
        else:
            print("Session expirée")
