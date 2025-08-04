from views.common_view import CommonView


class CreateClientView(CommonView):

    def input_datas():

        nom_complet = input("nom complet: ")
        email = input("email: ")
        telephone = input("téléphone: ")
        entreprise = input("entreprise: ")
        commercial = input("id commercial")
