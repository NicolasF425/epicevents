from base_managing.CRUD import get_all_clients


class ShowClientsView:

    def display_clients():
        clients = get_all_clients()

        for client in clients:
            id = client.id
            entreprise = client.nom_entreprise
            print(str(id)+" "+entreprise)
