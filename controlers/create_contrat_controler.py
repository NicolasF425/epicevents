from controlers.common_controler import CommonControler
from base_managing.CRUD import add_contrat
from base_managing.models import Contrat
from utilities.pause import pause


class CreateClientControler(CommonControler):

    def save_new_client(self, datas):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            contrat = Contrat()
            contrat.client_id = datas[0]
            contrat.commercial_id = datas[1]
            contrat.montant_total = datas[2]
            contrat.montant_restant = datas[3]
            contrat.est_signe = datas[4]
            add_contrat(contrat)
        else:
            from views.login_view import LoginView
            print("Session expirée")
            pause(3)
            view = LoginView()
            view.display_view()
