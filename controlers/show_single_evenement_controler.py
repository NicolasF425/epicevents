from controlers.common_controler import CommonControler


class ShowSingleEvenementControler(CommonControler):
    idCollaborateur = 0

    def check_action(self, action):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if action != "":
                pass
            else:
                # retour à la liste des collaborateurs
                from views.show_evenements_view import ShowEvenementsView
                view = ShowEvenementsView()
                view.display_evenements()
        else:
            print("Session expirée")
