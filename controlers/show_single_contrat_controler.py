from controlers.common_controler import CommonControler
from base_managing.CRUD import update_contrat


class ShowSingleContratControler(CommonControler):
    """
    Controler for the view ShowSingleContratView

    Used to manage user's actions
    """

    def check_action(self, action, id):
        """
        Manage the action defined in the view

        Args:
            action (string) : number of the field to modify
            id (int) : id of the 'contrat'
        """
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if action != "":
                from views.show_single_contrat_view import ShowSingleContratView
                view = ShowSingleContratView()
                view.display_update(action, id)
            else:
                # retour à la liste des contrats
                from views.show_contrats_view import ShowContratsView
                view = ShowContratsView()
                view.display_contrats()
        else:
            print("Session expirée")

    def save_new_value(self, idContrat, field, value):
        if idContrat > 0:
            update_contrat(idContrat, field, value)
            from views.show_contrats_view import ShowContratsView
            view = ShowContratsView()
            view.display_contrats()
