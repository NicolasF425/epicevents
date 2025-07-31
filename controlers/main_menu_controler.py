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
                # view "show_clients"
                pass
            case "show_contrats":
                # view "show_contrats"
                pass
            case "show_clients":
                # view "show_evenements"
                pass
