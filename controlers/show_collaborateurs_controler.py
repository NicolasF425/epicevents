from base_managing.CRUD import get_collaborateur_by_id
from controlers.common_controler import CommonControler
from views.show_single_collaborateur_view import ShowSingleCollaborateurView


class ShowCollaborateursControler(CommonControler):

    def select_action(self, id_collaborateur):
        if self.check_token_validity() is not False:
            if id_collaborateur != "":
                # selection d'une fiche collaborateur
                collaborateur = get_collaborateur_by_id(id_collaborateur)
                if collaborateur is not False:
                    view = ShowSingleCollaborateurView()
                    view.display_single_collaborateur(collaborateur)
            else:
                print("id incorrect !")
        else:
            print("Session expirée")
