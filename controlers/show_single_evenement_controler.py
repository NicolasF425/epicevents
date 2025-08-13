from controlers.common_controler import CommonControler
from base_managing.CRUD import update_evenement


class ShowSingleEvenementControler(CommonControler):
    idCollaborateur = 0

    def check_action(self, action, id):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if action != "":
                from views.show_single_evenement_view import ShowSingleEvenementView
                view = ShowSingleEvenementView()
                view.display_update(action, id)
            else:
                # retour à la liste des collaborateurs
                from views.show_evenements_view import ShowEvenementsView
                view = ShowEvenementsView()
                view.display_evenements()
        else:
            print("Session expirée")

    def save_new_value(idEvenement, field, value):
        if idEvenement > 0:
            update_evenement(id, field, value)
