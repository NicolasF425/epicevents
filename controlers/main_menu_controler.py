from views.show_clients_view import ShowClientsView
from views.show_contrats_view import ShowContratsView
from views.show_evenements_view import ShowEvenementsView
from views.show_collaborateurs_view import ShowCollaborateursView


class MainMenuControler:

    def select_action(self, num_action, mapping):

        for cle, valeur in mapping.items():
            if valeur == num_action:
                match cle:
                    case "manage_collaborateur":
                        view = ShowCollaborateursView()
                        view.display_collaborateurs()
                    case "add_support_evenement":
                        view = ShowEvenementsView()
                        view.display_evenements("evenements_sans_support")
                    case "my_clients":
                        view = ShowClientsView()
                        view.display_clients(True)
                    case "my_contrats":
                        view = ShowContratsView()
                        view.display_contrats(True)
                    case "my_evenements":
                        view = ShowEvenementsView()
                        view.display_evenements("mes_evenements")
                    case "show_clients":
                        view = ShowClientsView()
                        view.display_clients()
                    case "show_contrats":
                        view = ShowContratsView()
                        view.display_contrats()
                    case "show_evenements":
                        view = ShowEvenementsView()
                        view.display_evenements(True)
                    case "show_evenements":
                        view = ShowEvenementsView()
                        view.display_evenements()
                    case "quitter":
                        pass
