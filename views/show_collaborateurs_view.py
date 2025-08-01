from base_managing.CRUD import get_all_collaborateurs, get_nom_departement_by_id
from views.common_view import CommonView
from utilities.clear_screen import clear_screen


class ShowCollaborateursView(CommonView):

    def display_collaborateurs(self):
        collaborateurs = get_all_collaborateurs()

        clear_screen()
        print("COLLABORATEURS\n\n")
        print(f"{"║ id"[:5]:<5} | {"login"[:25]:<25} | {"email"[:25]:<25} | {"departement"[:20]:<20}"+"║\n")

        for collaborateur in collaborateurs:
            id = collaborateur.id
            login = collaborateur.login
            email = collaborateur.email
            nom_departement = get_nom_departement_by_id(collaborateur.departement_id)
            print(f"{"║ "+str(id)[:5]:<5} | {login[:25]:<25} | {email[:25]:<25} | {nom_departement[:20]:<20}║")

        input("")
