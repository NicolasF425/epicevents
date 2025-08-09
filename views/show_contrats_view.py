from base_managing.CRUD import get_all_contrats, get_client_by_id, get_contrats_by_idCommercial
from views.common_view import CommonView
from controlers.show_contrats_controler import ShowcontratsControler
from utilities.clear_screen import clear_screen
from utilities.constantes import COMMERCIAL_COLOR, RESET


class ShowContratsView(CommonView):
    controler = ShowcontratsControler()
    filtre = "mes contrats"

    def display_contrats(self, filtered=False):
        clear_screen()
        token = self.check_token_validity()

        if token is not False:
            if not filtered:
                print("CONTRATS\n\n")
                contrats = get_all_contrats()
            else:
                print(COMMERCIAL_COLOR+"MES CONTRATS\n\n"+RESET)
                contrats = get_contrats_by_idCommercial(token["id"])
            ids_contrats = []
            if contrats is not None:
                for contrat in contrats:
                    if (self.filtre == "mes contrats") or (self.filtre == "non signe" and contrat.est_signe is False) \
                            or (self.filtre == "non totalement paye" and contrat.montant_restant > 0):
                        id = contrat.id
                        ids_contrats.append(id)
                        client = contrat.client_id
                        nom_client = get_client_by_id(client).nom_entreprise
                        print(f"{"║ "+str(id)[:5]:<5} | {nom_client[:30]:<30} ║")

            print("\n 1) Créer un nouveau contrat")
            print(" 2) Modifier un contrat")
            print(" 3) Supprimer un contrat")

            print("\n 4) aucun filtre")
            print(" 5) afficher non signés")
            print(" 6) afficher non tatalement payés")
            choix = input("\nEntrez le numéro d'une action "
                          "ou appuyez sur Entrée pour retourner au menu : ")
            if choix in ["1", "2", "3"]:
                if choix == "1":
                    contrat = 0
                elif choix == "2":
                    contrat = input("Entrez l'id du contrat à modifier: ")
                    int_contrat = int(contrat)
                    if int_contrat not in ids_contrats:
                        print("id incorrect")
                        contrat = 0
                elif choix == "3":
                    contrat = input("Entrez l'id du contrat à supprimer: ")
                    int_contrat = int(contrat)
                    if int_contrat not in ids_contrats:
                        print("id incorrect")
                        contrat = 0
                else:
                    choix = ""
                    contrat = 0
                self.controler.select_action(choix, contrat)
            if choix in ["4", "5", "6"]:
                self.controler.select_action(choix, 0)
        else:
            print("Session expirée")
