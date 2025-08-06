from controlers.common_controler import CommonControler
from base_managing.CRUD import update_contrat


class ShowSingleContratControler(CommonControler):
    idCollaborateur = 0

    def check_action(self, action):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if action != "":
                pass
            else:
                # retour à la liste des contrats
                from views.show_contrats_view import ShowContratsView
                view = ShowContratsView()
                view.display_contrats()
        else:
            print("Session expirée")

    def save_new_value(idContrat, field, value):
        if idContrat > 0:
            update_contrat(id, field, value)
