from base_managing.initialisation_base import Collaborateur
from base_managing.CRUD import add_collaborateur


collab1 = Collaborateur(login="Joe123", password="Azerty123,;:", email="joe@epic-events.com",
                        departement_id="1")


# Création de données de base
add_collaborateur(collab1)
