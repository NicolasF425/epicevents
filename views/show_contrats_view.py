from base_managing.CRUD import get_all_contrats


class ShowContratsView:

    def display_contrats():
        contrats = get_all_contrats()

        for contrat in contrats:
            id = contrat.id
            client = contrat.client
            print(str(id)+" "+client)
