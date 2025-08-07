from controlers.common_controler import CommonControler
from base_managing.CRUD import add_evenement
from base_managing.models import Evenement
from utilities.pause import pause


class CreateEvenementControler(CommonControler):

    def save_new_client(self, datas):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            evenement = Evenement()
            evenement.nom = datas[0]
            evenement.client_id = datas[1]
            evenement.contrat_id = datas[2]
            evenement.responsable_support_id = None
            add_evenement(evenement)
        else:
            from views.login_view import LoginView
            print("Session expirée")
            pause(3)
            view = LoginView()
            view.display_view()
