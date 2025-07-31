from base_managing.initialisation_base import Collaborateur
from base_managing.CRUD import add_collaborateur


collab1 = Collaborateur(login="Joe123", password="Azerty123,;:", email="joe@epic-events.com",
                        departement_id="1")
collab2 = Collaborateur(login="Tom456", password="Azerty456,;:", email="tom@epic-events.com",
                        departement_id="2")
collab3 = Collaborateur(login="Bob789", password="Azerty789,;:", email="bob@epic-events.com",
                        departement_id="3")


# Création de données de base
add_collaborateur(collab1)
add_collaborateur(collab2)
add_collaborateur(collab3)
