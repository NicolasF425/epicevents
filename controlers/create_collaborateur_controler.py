from controlers.common_controler import CommonControler
from base_managing.CRUD import add_collaborateur
from base_managing.models import Collaborateur
from utilities.pause import pause


class CreateCollaborateurControler(CommonControler):

    def save_new_collaborateur(self, datas):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            collaborateur = Collaborateur()
            collaborateur.login = datas[0]
            collaborateur.password = datas[1]
            collaborateur.email = datas[2]
            collaborateur.departement_id = datas[3]
            add_collaborateur(collaborateur)
            print("Nouveau collaborateur créé")
            from views.show_collaborateurs_view import ShowCollaborateursView
            view = ShowCollaborateursView()
            view.display_collaborateurs()
        else:
            from views.login_view import LoginView
            print("Session expirée")
            pause(3)
            view = LoginView()
            view.display_view()
