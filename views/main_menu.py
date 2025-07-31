from utilities.gestion_token import JWTManager
from controlers.main_menu_controler import MainMenuControler


class main_menu_view:
    num = 1
    mapping = {}
    controler = MainMenuControler()

    def check_token_validity(self):
        jwt = JWTManager()
        token = jwt.read_token()
        token_is_valid = jwt.verify_token(token)
        if token_is_valid:
            return token
        else:
            return False

    def item_create_collaborateur(self):
        token = self.check_token_validity()
        if token is not False:
            departement_id = token["departement_id"]
            # si gestion
            if departement_id == 3:
                print(str(self.num)+") Gérer les collaborateurs")
                self.num += 1
                self.mapping["create_collaborateur"] = self.num

    def item_show_clients(self):
        token = self.check_token_validity()
        if token is not False:
            print(str(self.num)+") Lister les clients")
            self.num += 1
            self.mapping["show_clients"] = self.num

    def item_show_contrats(self):
        token = self.check_token_validity()
        if token is not False:
            print(str(self.num)+") Lister les contrats")
            self.num += 1
            self.mapping["show_contrats"] = self.num

    def item_show_evenements(self):
        token = self.check_token_validity()
        if token is not False:
            print(str(self.num)+") Lister les évènements")
            self.num += 1
            self.mapping["show_evenements"] = self.num

    def select_action(self):
        num_action = str(input("Numéro d'action: "))
        if num_action > 0 and num_action <= self.num:
            self.controler.select_action(num_action, self.mapping)
