from controlers.common_controler import CommonControler
from base_managing.CRUD import update_collaborateur


class ShowSingleCollaborateursControler(CommonControler):

    def check_action(self, action, id):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if action != "":
                # modification d'un champ
                from views.show_single_collaborateur_view import ShowSingleCollaborateurView
                view = ShowSingleCollaborateurView()
                view.display_update(action, id)
            else:
                # retour à la liste des collaborateurs
                from views.show_collaborateurs_view import ShowCollaborateursView
                view = ShowCollaborateursView()
                view.display_collaborateurs()
        else:
            print("Session expirée")

    def save_new_value(self, idCollaborateur, field, value):
        if idCollaborateur > 0:
            update_collaborateur(idCollaborateur, field, value)

        # retour à la liste des collaborateurs
        from views.show_collaborateurs_view import ShowCollaborateursView
        view = ShowCollaborateursView()
        view.display_collaborateurs()
