from controlers.common_controler import CommonControler
from base_managing.CRUD import update_collaborateur


class ShowSingleCollaborateursControler(CommonControler):
    idCollaborateur = 0

    def check_action(self, action):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if action != "":
                # modification d'un champ
                from views.show_single_collaborateur_view import ShowSingleCollaborateurView
                view = ShowSingleCollaborateurView()
                view.display_update(action)
            else:
                # retour à la liste des collaborateurs
                from views.show_collaborateurs_view import ShowCollaborateursView
                view = ShowCollaborateursView()
                view.display_collaborateurs()
        else:
            print("Session expirée")

    def save_new_value(idCollaborateur, field, value):
        if idCollaborateur > 0:
            update_collaborateur(id, field, value)
