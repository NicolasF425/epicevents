from controlers.common_controler import CommonControler


class ShowSingleContratControler(CommonControler):
    idCollaborateur = 0

    def check_action(self, action):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if action != "":
                pass
            else:
                # retour à la liste des collaborateurs
                from views.show_contrats_view import ShowContratsView
                view = ShowContratsView()
                view.display_contrats()
        else:
            print("Session expirée")
