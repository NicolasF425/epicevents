from base_managing.models import Collaborateur, Client, Contrat, Evenement
from base_managing.CRUD import add_collaborateur, add_client, add_contrat, add_evenement
from datetime import datetime


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

contrat1 = Contrat(client_id=1, commercial_id=1, montant_total=5000.56, montant_restant=2500.25)

evenement1 = Evenement(nom="Journée spéciale plantes vertes", client_id=1, contrat_id=1,
                       date_debut=datetime(2026, 8, 15, 10, 30, 0),
                       date_fin=datetime(2026, 8, 16, 19, 30, 0),
                       lieu="en magasin",
                       adresse_lieu="3 allée des platanes, 44000 NANTES",
                       nombre_participants=6,
                       notes="Animation chez le client")


# Création de données initiales

add_collaborateur(collab1)
add_collaborateur(collab2)
add_collaborateur(collab3)

add_client(client1)
add_client(client2)

add_contrat(contrat1)

add_evenement(evenement1)
