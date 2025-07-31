from views.show_clients_view import ShowClientsView
from views.show_contrats_view import ShowContratsView
from views.show_evenements_view import ShowEvenementsView


class MainMenuControler:

    def select_action(self, num_action, mapping):
        for cle, valeur in mapping.items():
            if valeur == num_action:
                action = cle

        match action:
            case "create_collaborateur":
                # view "create_collaborateur"
                pass
            case "show_clients":
                view = ShowClientsView()
                view.display_clients()
            case "show_contrats":
                view = ShowContratsView()
                view.display_contrats()
            case "show_evenements":
                view = ShowEvenementsView()
                view.display_evenements()
            case "quitter":
                pass
