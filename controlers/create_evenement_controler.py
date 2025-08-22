from controlers.common_controler import CommonControler
from base_managing.CRUD import add_evenement
from base_managing.models import Evenement
from utilities.pause import pause


class CreateEvenementControler(CommonControler):

    def save_new_evenement(self, datas):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            evenement = Evenement()
            evenement.nom = datas[0]
            evenement.client_id = datas[1]
            evenement.contrat_id = datas[2]
            evenement.responsable_support_id = None
            evenement.lieu = datas[4]
            evenement.adresse_lieu = datas[5]
            evenement.nombre_participants = datas[6]
            add_evenement(evenement)
            from views.show_evenements_view import ShowEvenementsView
            view = ShowEvenementsView()
            view.display_evenements()
        else:
            from views.login_view import LoginView
            print("Session expirée")
            pause(3)
            view = LoginView()
            view.display_view()
