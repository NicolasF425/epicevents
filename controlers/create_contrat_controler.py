from controlers.common_controler import CommonControler
from base_managing.CRUD import add_contrat
from base_managing.models import Contrat
from utilities.constantes import GESTION


class CreateContratControler(CommonControler):

    def save_new_contrat(self, datas):
        # si le token est toujours valide
        token = self.check_token_validity()
        if token is not False:
            if token['departement_id'] == GESTION:
                contrat = Contrat()
                contrat.client_id = datas[0]
                contrat.commercial_id = datas[1]
                contrat.montant_total = datas[2]
                contrat.montant_restant = datas[3]
                contrat.est_signe = datas[4]
                add_contrat(contrat)
                from views.show_contrats_view import ShowContratsView
                view = ShowContratsView()
                view.display_contrats()
        else:
            print("Session expirée")
