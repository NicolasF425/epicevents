from initialisation_base import Collaborateur, Client, Contrat, Evenement
from CRUD import add_collaborateur, add_client


collab1 = Collaborateur(login="Joe123", password="Azerty123,;:", email="joe@epic-events.com",
                        departement_id="1")


# Création de données de base
add_collaborateur(collab1)
