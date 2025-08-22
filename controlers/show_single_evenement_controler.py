from controlers.common_controler import CommonControler
from utilities.constantes import SUPPORT, GESTION
from base_managing.CRUD import update_evenement


class ShowSingleEvenementControler(CommonControler):

    def check_action(self, element, idEvenement, idSupport, departementId):

        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if element != "":
                if departementId == SUPPORT:
                    from views.show_single_evenement_view import ShowSingleEvenementView
                    view = ShowSingleEvenementView()
                    view.display_update(element, idEvenement)
                if departementId == GESTION:
                    self.save_new_value(idEvenement, "responsable_support_id", idSupport)
                    # retour à la liste des evenements
                    from views.show_evenements_view import ShowEvenementsView
                    view = ShowEvenementsView()
                    view.display_evenements("evenements_sans_support")
            else:
                # retour à la liste des evenements
                from views.show_evenements_view import ShowEvenementsView
                view = ShowEvenementsView()
                view.display_evenements()
        else:
            print("Session expirée")

    def save_new_value(self, idEvenement, field, value):
        if idEvenement > 0:
            update_evenement(idEvenement, field, value)
            from views.show_evenements_view import ShowEvenementsView
            view = ShowEvenementsView()
            view.display_evenements()
