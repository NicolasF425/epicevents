from sqlalchemy import select, update, delete
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from base_managing.initialisation_base import Collaborateur, Client, Contrat, Evenement
from utilities.gestion_hashage import hash_password
from base_managing.params import PASSWORD


Base = declarative_base()


def create_session():
    pwd = PASSWORD

    # Configuration de la base de données
    username = "root"
    password = quote(pwd)  # encode les caractères spéciaux
    host = "localhost"
    port = 3306
    dbname = "epicevents"

    DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}"

    engine = create_engine(DATABASE_URL, echo=False)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    with SessionLocal() as session:
        return session


# CREATE


def add_collaborateur(collaborateur):
    try:
        session = create_session()
        collaborateur.password = hash_password(collaborateur.password)
        session.add(collaborateur)
        session.commit()
    finally:
        session.close()


def add_client(client):
    try:
        session = create_session()
        session.add(client)
        session.commit()
    finally:
        session.close()


def add_evenement(evenement):
    try:
        session = create_session()
        session.add(evenement)
        session.commit()
    finally:
        session.close()


def add_contrat(contrat):
    try:
        session = create_session()
        session.add(contrat)
        session.commit()
    finally:
        session.close()

# READ


def get_collaborateur_by_id(idCollaborateur):
    session = create_session()
    selection = select(Collaborateur).where(Collaborateur.id == idCollaborateur)
    result = session.execute(selection)
    collaborateur = result.scalars().one()
    return collaborateur


def get_collaborateur_by_login(loginCollaborateur):
    session = create_session()
    selection = select(Collaborateur).where(Collaborateur.login == loginCollaborateur)
    result = session.execute(selection)
    collaborateur = result.scalars().one()
    return collaborateur


def get_all_clients():
    session = create_session()
    selection = select(Client)
    result = session.execute(selection)
    all_clients = result.scalars().all()
    return all_clients


def get_all_contrats():
    session = create_session()
    selection = select(Contrat)
    result = session.execute(selection)
    all_contrats = result.scalars().all()
    return all_contrats


def get_all_evenements():
    session = create_session()
    selection = select(Evenement)
    result = session.execute(selection)
    all_evenements = result.scalars().all()
    return all_evenements


def get_client_by_id(idClient):
    session = create_session()
    selection = select(Client).where(Client.id == idClient)
    result = session.execute(selection)
    client = result.scalars().one()
    return client


def get_clients_by_idCommercial(idCollab):
    session = create_session()
    selection = select(Client).where(Client.commercial_id == idCollab)
    result = session.execute(selection)
    clients = result.scalars().all()
    return clients


def get_contrats_by_idCommercial(idCollab):
    session = create_session()
    selection = select(Contrat).where(Contrat.commercial_id == idCollab)
    result = session.execute(selection)
    contrats = result.scalars().all()
    return contrats


def get_evenements_by_idSupport(idCollab):
    session = create_session()
    selection = select(Evenement).where(Evenement.responsable_support_id == idCollab)
    result = session.execute(selection)
    evenements = result.scalars().all()
    return evenements


# UPDATE


def update_client(idClient, aModifier, nouvelleValeur):
    session = create_session()

    match aModifier:
        case "nom_complet":
            stmt = update(Client).where(Client.id == idClient).values(nom_complet=nouvelleValeur)
        case "email":
            stmt = update(Client).where(Client.id == idClient).values(email=nouvelleValeur)
        case "telephone":
            stmt = update(Client).where(Client.id == idClient).values(telephone=nouvelleValeur)
        case "nom_entreprise":
            stmt = update(Client).where(Client.id == idClient).values(nom_entreprise=nouvelleValeur)
    try:
        session.execute(stmt)
        session.commit()
    finally:
        session.close()


def update_contrat(idContrat, aModifier, nouvelleValeur):
    session = create_session()

    match aModifier:
        case "client_id":
            stmt = update(Client).where(Client.id == idContrat).values(client_id=nouvelleValeur)
        case "commercial_id":
            stmt = update(Client).where(Client.id == idContrat).values(montant_total=nouvelleValeur)
        case "montant_total":
            stmt = update(Client).where(Client.id == idContrat).values(telephone=nouvelleValeur)
        case "montant_restant":
            stmt = update(Client).where(Client.id == idContrat).values(montant_restant=nouvelleValeur)
        case "statut_id":
            stmt = update(Client).where(Client.id == idContrat).values(statut_id=nouvelleValeur)
        case "date_signature":
            stmt = update(Client).where(Client.id == idContrat).values(date_signature=nouvelleValeur)
        case "date_fin_prevue":
            stmt = update(Client).where(Client.id == idContrat).values(date_fin_prevue=nouvelleValeur)
    try:
        session.execute(stmt)
        session.commit()
    finally:
        session.close()


def update_evenement(idEvenement, aModifier, nouvelleValeur):
    session = create_session()

    match aModifier:
        case "nom":
            stmt = update(Evenement).where(Evenement.id == idEvenement).values(nom=nouvelleValeur)
        case "contrat_id":
            stmt = update(Evenement).where(Evenement.id == idEvenement).values(contrat_id=nouvelleValeur)
        case "responsable_support_id":
            stmt = update(Evenement).where(Evenement.id == idEvenement).values(responsable_support_id=nouvelleValeur)
        case "date_debut":
            stmt = update(Evenement).where(Evenement.id == idEvenement).values(date_debut=nouvelleValeur)
        case "date_fin":
            stmt = update(Evenement).where(Evenement.id == idEvenement).values(date_fin=nouvelleValeur)
        case "lieu":
            stmt = update(Evenement).where(Evenement.id == idEvenement).values(lieu=nouvelleValeur)
        case "adresse_lieu":
            stmt = update(Evenement).where(Evenement.id == idEvenement).values(adresse_lieu=nouvelleValeur)
        case "nombre_participants":
            stmt = update(Evenement).where(Evenement.id == idEvenement).values(nombre_participants=nouvelleValeur)
        case "statut_id":
            stmt = update(Evenement).where(Evenement.id == idEvenement).values(statut_id=nouvelleValeur)
        case "notes":
            stmt = update(Evenement).where(Evenement.id == idEvenement).values(notes=nouvelleValeur)
    try:
        session.execute(stmt)
        session.commit()
    finally:
        session.close()


# DELETE


def delete_client(idClient):
    session = create_session()
    stmt = delete(Client).where(Client.id == idClient)
    try:
        session.execute(stmt)
        session.commit()
    finally:
        session.close()


def delete_contrat(idContrat):
    session = create_session()
    stmt = delete(Contrat).where(Contrat.id == idContrat)
    try:
        session.execute(stmt)
        session.commit()
    finally:
        session.close()


def delete_evenement(idEvenement):
    session = create_session()
    stmt = delete(Evenement).where(Evenement.id == idEvenement)
    try:
        session.execute(stmt)
        session.commit()
    finally:
        session.close()
