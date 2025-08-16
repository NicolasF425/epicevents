from controlers.main_menu_controler import MainMenuControler
from views.common_view import CommonView
from utilities.constantes import COMMERCIAL, GESTION, SUPPORT
from utilities.constantes import COMMERCIAL_COLOR, SUPPORT_COLOR, RESET
from utilities.clear_screen import clear_screen


class MainMenuView(CommonView):
    num = 0
    mapping = {}
    controler = MainMenuControler()

    def build_menu(self):
        token = self.check_token_validity()

        # listage des elements à afficher et des actions possibles
        if token is not False:
            # gestion collaborateurs
            departement_id = token["departement_id"]
            # si departement gestion
            if departement_id == GESTION:
                self.num += 1
                self.mapping["manage_collaborateur"] = self.num
                self.num += 1
                self.mapping["add_support_evenement"] = self.num
            # si departement commercial
            if departement_id == COMMERCIAL:
                self.num += 1
                self.mapping["my_clients"] = self.num
                self.num += 1
                self.mapping["my_contrats"] = self.num
            # liste des clients
            self.num += 1
            self.mapping["show_clients"] = self.num
            # liste des contrats
            self.num += 1
            self.mapping["show_contrats"] = self.num
            # si departement support
            if departement_id == SUPPORT:
                self.num += 1
                self.mapping["my_evenements"] = self.num
            # liste des evenements
            self.num += 1
            self.mapping["show_evenements"] = self.num
            # quitter
            self.num += 1
            self.mapping["quitter"] = self.num
        else:
            print("Erreur de token")

    def item_manage_collaborateur(self, num):
        print(SUPPORT_COLOR+str(num)+") Gérer les collaborateurs"+RESET)

    def item_add_support_evenement(self, num):
        print(SUPPORT_COLOR+str(num)+") Affecter un support à un événement"+RESET)

    def item_my_clients(self, num):
        print(COMMERCIAL_COLOR+str(num)+") Mes clients"+RESET)

    def item_my_contrats(self, num):
        print(COMMERCIAL_COLOR+str(num)+") Mes contrats"+RESET)

    def item_my_evenements(self, num):
        print(SUPPORT_COLOR+str(num)+") Mes évènements"+RESET)

    def item_show_clients(self, num):
        print(str(num)+") Lister les clients")

    def item_show_contrats(self, num):
        print(str(num)+") Lister les contrats")

    def item_show_evenements(self, num):
        print(str(num)+") Lister les évènements")

    def item_quitter(self, num):
        print(str(num)+") Quitter")

    def display_items(self):
        clear_screen()
        self.build_menu()
        print("MENU PRINCIPAL\n\n")
        # cle = action
        # valeur = numéro associé
        for cle, valeur in self.mapping.items():
            match cle:
                case "manage_collaborateur":
                    self.item_manage_collaborateur(valeur)
                case "add_support_evenement":
                    self.item_add_support_evenement(valeur)
                case "my_clients":
                    self.item_my_clients(valeur)
                case "my_contrats":
                    self.item_my_contrats(valeur)
                case "my_evenements":
                    self.item_my_evenements(valeur)
                case "show_clients":
                    self.item_show_clients(valeur)
                case "show_contrats":
                    self.item_show_contrats(valeur)
                case "my_evenements":
                    self.item_my_evenements(valeur)
                case "show_evenements":
                    self.item_show_evenements(valeur)
                case "quitter":
                    self.item_quitter(valeur)

        num_action = int(input("Numéro d'action: "))
        if num_action > 0 and num_action <= self.num:
            self.controler.select_action(num_action, self.mapping)
