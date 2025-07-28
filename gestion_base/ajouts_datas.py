from initialisation_base import Collaborateur
from CRUD import add_collaborateur


collab1 = Collaborateur(login="Joe123", password="Azerty123,;:", email="joe@epic-events.com",
                        departement_id="1")


# Création de données de base
add_collaborateur(collab1)
