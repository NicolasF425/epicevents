from views.common_view import CommonView
from utilities.clear_screen import clear_screen
from controlers.show_single_evenement_controler import ShowSingleEvenementControler
from base_managing.CRUD import get_collaborateurs_by_idDepartement
from utilities.constantes import SUPPORT, GESTION


class ShowSingleEvenementView(CommonView):
    '''
    View to display and mofification of a single "evenement"

    Use the controler `ShowSingleEvenementControler` to
    manage user's actions
    '''
    controler = ShowSingleEvenementControler()

    def display_single_evenement(self, evenement, update=False):
        clear_screen()
        token = self.check_token_validity()

        if token is not False:
            if token['departement_id'] == SUPPORT and update:
                idSupport = 0
                print("DONNEES EVENEMENT\n\n")
                print(" id: "+str(evenement.id))
                print(" 1) nom: "+evenement.nom)
                print(" 2) id client: "+str(evenement.client_id))
                print(" 3) id contrat: "+str(evenement.contrat_id))
                print(" Id responsable support: "+str(evenement.responsable_support_id))
                print(f" 4) date début: {evenement.date_debut.strftime('%d-%m-%Y %H:%M:%S')}")
                print(f" 5) date fin: {evenement.date_fin.strftime('%d-%m-%Y %H:%M:%S')}")
                print(" 6) Lieu: "+evenement.lieu+" "+evenement.adresse_lieu)
                print(" 7) Attendus: "+str(evenement.nombre_participants))
                print(" 8) Notes: "+evenement.notes)
                element = input("\nEntrez le numéro de l'élément à "
                                "modifier ou appyez sur Entrée pour revenir au menu: ")
            elif token['departement_id'] == GESTION and update:
                element = 0
                collaborateurs = get_collaborateurs_by_idDepartement(SUPPORT)
                print(f"{"║ id"[:5]:<5} | {"login"[:25]:<25} | {"email"[:25]:<25} ║\n")
                ids_collaborateurs = []
                for collaborateur in collaborateurs:
                    id = collaborateur.id
                    ids_collaborateurs.append(id)
                    login = collaborateur.login
                    email = collaborateur.email
                    print(f"{"║ "+str(id)[:5]:<5} | {login[:25]:<25} | {email[:25]:<25} ║")
                print("\nEntrez le numéro de collaborateur support à affecter")
                inputIdSupport = input("ou appuyez sur Entrée pour revenir au menu: ")
                if inputIdSupport != "":
                    idSupport = int(inputIdSupport)
            else:
                print("DONNEES EVENEMENT\n\n")
                print(" id: "+str(evenement.id))
                print(" nom: "+evenement.nom)
                print(" id client: "+str(evenement.client_id))
                print(" id contrat: "+str(evenement.contrat_id))
                print("Id responsable support: "+str(evenement.responsable_support_id))
                print(f" date début: {evenement.date_debut.strftime('%d-%m-%Y %H:%M:%S')}")
                print(f" date fin: {evenement.date_fin.strftime('%d-%m-%Y %H:%M:%S')}")
                print(" Lieu: "+evenement.lieu+" "+evenement.adresse_lieu)
                print(" Attendus: "+str(evenement.nombre_participants))
                print(" Notes: "+evenement.notes)
                input("\n Appuyez sur Entrée pour revenir au menu: ")
                element = ""
                idSupport = 0

            self.controler.check_action(element, evenement.id, idSupport, token['departement_id'])

    def display_update(self, field_number, id):
        print("\n")
        infos = []
        match field_number:
            case "1":
                new_nom = input("nouveau nom: ")
                infos = ["nom", new_nom]
            case "2":
                new_id_client = input("nouvel id client : ")
                infos = ["client_id", new_id_client]
            case "3":
                new_contrat_id = input("nouvel id contrat: ")
                infos = ["contrat_id", new_contrat_id]
            case "4":
                new_date_debut = input("nouvelle date début, au format AAAA-MM-JJ HH:MM:SS: ")
                infos = ["date_debut", new_date_debut]
            case "5":
                new_date_fin = input("nouvelle date fin, au format AAAA-MM-JJ HH:MM:SS: ")
                infos = ["date_fin", new_date_fin]
            case "6":
                new_lieu = input("nouveau lieu: ")
                infos = ["nom", new_lieu]
            case "7":
                new_adresse = input("nouvelle adresse : ")
                infos = ["adresse_lieu", new_adresse]
            case "8":
                new_notes = input("nouvelles notes: ")
                infos = ["notes", new_notes]

        if self.controler.check_token_validity() is not False:
            if infos:
                self.controler.save_new_value(id, infos[0], infos[1])
