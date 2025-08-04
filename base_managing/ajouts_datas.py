from base_managing.models import Collaborateur, Client
from base_managing.CRUD import add_collaborateur, add_client


collab1 = Collaborateur(login="Joe123", password="Azerty123,;:", email="joe@epic-events.com",
                        departement_id="1")
collab2 = Collaborateur(login="Tom456", password="Azerty456,;:", email="tom@epic-events.com",
                        departement_id="2")
collab3 = Collaborateur(login="Bob789", password="Azerty789,;:", email="bob@epic-events.com",
                        departement_id="3")

client1 = Client(nom_complet="Jean Martin", email="jm@martin.fr", telephone="0102030405",
                 nom_entreprise="Martin jardinerie", commercial_id=1)
client2 = Client(nom_complet="Pierre Denis", email="pierre.denis@brico.fr", telephone="0203040501",
                 nom_entreprise="Denis bricolage", commercial_id=1)


# Création de données initiales
add_collaborateur(collab1)
add_collaborateur(collab2)
add_collaborateur(collab3)

add_client(client1)
add_client(client2)
