from base_managing.CRUD import get_all_contrats, get_client_by_id, get_contrats_by_idCommercial
from views.common_view import CommonView
from controlers.show_contrats_controler import ShowcontratsControler
from utilities.clear_screen import clear_screen
from utilities.constantes import GESTION, COMMERCIAL, GESTION_COLOR, COMMERCIAL_COLOR, RESET


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
                print(f"{"║ "+"id"[:5]:<5} | {"nom client"[:30]:<30} | {"montant restant"[:15]:<15} \
                              | {"est signe"[:10]:<10} ║\n")
                for contrat in contrats:
                    if (self.filtre == "mes contrats") or (self.filtre == "non signe" and contrat.est_signe is False) \
                            or (self.filtre == "non totalement paye" and contrat.montant_restant > 0):
                        id = contrat.id
                        ids_contrats.append(id)
                        client = contrat.client_id
                        nom_client = get_client_by_id(client).nom_entreprise
                        montant_restant = contrat.montant_restant
                        est_signe = "non"
                        if contrat.est_signe:
                            est_signe = "oui"
                        print(f"{"║ "+str(id)[:5]:<5} | {nom_client[:30]:<30} | {str(montant_restant)[:15]:<15} \
                              | {est_signe[:10]:<10} ║")

            compteur = 1
            create = False
            update = False
            if token['departement_id'] == GESTION:
                print("\n "+GESTION_COLOR+str(compteur)+") Créer un nouveau contrat"+RESET)
                compteur += 1
                create = True
            if (token['departement_id'] == GESTION and filtered is False) or \
               (token['departement_id'] == COMMERCIAL and filtered is True):
                print("\n "+str(compteur)+") Modifier un contrat")
                compteur += 1
                update = True
            else:
                print("\n "+str(compteur)+") Voir les détail d'un contrat")
                compteur += 1
            if token['departement_id'] == GESTION:
                print("\n "+GESTION_COLOR+str(compteur)+") Supprimer un contrat"+RESET)
                compteur += 1
            if token['departement_id'] == COMMERCIAL and filtered is True:
                print("\n "+str(compteur)+") aucun filtre")
                print(" "+str(compteur+1)+") afficher non signés")
                print(" "+str(compteur+2)+") afficher non totalement payés")

            choix = input("\nEntrez le numéro d'une action "
                          "ou appuyez sur Entrée pour retourner au menu : ")

            if choix == "1" and create is True:  # GESTION
                contrat = 0
                self.controler.select_action(choix, contrat, update)
            elif choix == "1" and create is False and update is True:  # COMMERCIAL
                contrat = input("Entrez l'id du contrat à modifier: ")
                int_contrat = int(contrat)
                if int_contrat not in ids_contrats:
                    print("id incorrect")
                    contrat = 0
                self.controler.select_action(choix, contrat, update)
            elif choix == "1" and create is False and update is False:  # SUPPORT
                contrat = input("Entrez l'id du contrat: ")
                int_contrat = int(contrat)
                if int_contrat not in ids_contrats:
                    print("id incorrect")
                    contrat = 0
                self.controler.select_action(choix, contrat, update)
            elif choix == "2" and create is True and update is True:    # GESTION
                contrat = input("Entrez l'id du contrat à modifier: ")
                int_contrat = int(contrat)
                if int_contrat not in ids_contrats:
                    print("id incorrect")
                    contrat = 0
                self.controler.select_action(choix, contrat, update)
            elif choix in ["2", "3", "4"] and token['departement_id'] == COMMERCIAL:
                self.controler.select_action(choix, 0)
            elif choix == "3" and token['departement_id'] == GESTION:   # si suppression
                contrat = input("Entrez l'id du contrat à supprimer: ")
                self.controler.select_action(choix, contrat, update)
            else:
                choix = ""
                contrat = 0
                self.controler.select_action(choix, contrat, update)
        else:
            print("Session expirée")
