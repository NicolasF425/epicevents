from controlers.common_controler import CommonControler


class ShowSingleCollaborateursControler(CommonControler):

    def select_action(self, collaborateur):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if collaborateur != "":
                pass
            else:
                # retour à la liste des collaborateurs
                from views.show_collaborateurs_view import ShowCollaborateursView
                view = ShowCollaborateursView()
                view.display_collaborateurs()
        else:
            print("Session expirée")
