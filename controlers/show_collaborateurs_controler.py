from base_managing.CRUD import get_collaborateur_by_id, get_collaborateur_by_login, delete_collaborateur
from controlers.common_controler import CommonControler
from views.show_single_collaborateur_view import ShowSingleCollaborateurView


class ShowCollaborateursControler(CommonControler):

    def select_action(self, collaborateur):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if collaborateur != "":
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
                    if get_collaborateur_by_login(collaborateur) is not False:
                        delete_collaborateur(collaborateur)
                        print("Collaborateur supprimé")
                    else:
                        print("Login non trouvé")
            else:
                # retour au menu
                from views.main_menu_view import MainMenuView
                view = MainMenuView()
                view.display_items()
        else:
            print("Session expirée")
