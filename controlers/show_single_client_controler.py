from controlers.common_controler import CommonControler


class ShowSingleClientControler(CommonControler):
    idCollaborateur = 0

    def check_action(self, action):
        # si le token est toujours valide
        if self.check_token_validity() is not False:
            if action != "":
                pass
            else:
                # retour à la liste des clients
                from views.show_clients_view import ShowClientsView
                view = ShowClientsView()
                view.display_clients()
        else:
            print("Session expirée")

    def display_update(self, field_number):
        print("\n")
        match field_number:
            case 1:
                new_login = input("nouveau login: ")
                return "login", new_login
            case 2:
                new_password = input("nouveau mot de passe: ")
                return "password", new_password
            case 3:
                new_email = input("nouvel email: ")
                return "email", new_email
            case 4:
                new_departement_id = int(input("nouvel id departement: "))
                return "departement_id", new_departement_id
        if self.controler.check_token_validity() is not False:
            self.controler.save_new_value()
