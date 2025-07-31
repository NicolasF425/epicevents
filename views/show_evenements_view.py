from base_managing.CRUD import get_all_evenements


class ShowEvenementsView:

    def display_evenements():
        evenements = get_all_evenements()

        for evenement in evenements:
            id = evenement.id
            nom = evenement.nom
            print(str(id)+" "+nom)
