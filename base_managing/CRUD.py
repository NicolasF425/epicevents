from sqlalchemy import select, update, delete
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import NoResultFound
from base_managing.models import Collaborateur, Client, Contrat, Evenement, Departement
from utilities.gestion_hashage import hash_password
from base_managing.params import PASSWORD


Base = declarative_base()


def create_session():
    # Configuration de la base de données
    username = "root"
    password = quote(PASSWORD)  # encode les caractères spéciaux
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


def get_all_collaborateurs():
    session = create_session()
    selection = select(Collaborateur)
    result = session.execute(selection)
    all_collaborateurs = result.scalars().all()
    return all_collaborateurs


def get_all_clients():
    session = create_session()
    selection = select(Client)
    result = session.execute(selection)
    all_clients = result.scalars().all()
    session.close()
    return all_clients


def get_all_contrats():
    session = create_session()
    selection = select(Contrat)
    result = session.execute(selection)
    all_contrats = result.scalars().all()
    session.close()
    return all_contrats


def get_all_evenements():
    session = create_session()
    selection = select(Evenement)
    result = session.execute(selection)
    all_evenements = result.scalars().all()
    session.close()
    return all_evenements


def get_collaborateur_by_id(idCollaborateur):
    try:
        session = create_session()
        selection = select(Collaborateur).where(Collaborateur.id == idCollaborateur)
        result = session.execute(selection)
        collaborateur = result.scalars().one()
        return collaborateur
    except NoResultFound:
        print("collaborateur non trouvé")
        return False
    finally:
        if session:
            session.close()


def get_collaborateur_by_login(loginCollaborateur):
    try:
        session = create_session()
        selection = select(Collaborateur).where(Collaborateur.login == loginCollaborateur)
        result = session.execute(selection)
        collaborateur = result.scalars().one()
        return collaborateur
    except NoResultFound:
        print("collaborateur non trouvé")
        return False
    finally:
        if session:
            session.close()


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


def get_contrat_by_id(id):
    session = create_session()
    selection = select(Contrat).where(Contrat.id == id)
    result = session.execute(selection)
    contrat = result.scalars().one()
    return contrat


def get_evenements_by_idSupport(idCollab):
    session = create_session()
    selection = select(Evenement).where(Evenement.responsable_support_id == idCollab)
    result = session.execute(selection)
    evenements = result.scalars().all()
    return evenements


def get_evenements_by_id(id):
    session = create_session()
    selection = select(Evenement).where(Evenement.id == id)
    result = session.execute(selection)
    evenement = result.scalars().one()
    return evenement


def get_nom_departement_by_id(idDepartement):
    session = create_session()
    selection = select(Departement).where(Departement.id == idDepartement)
    result = session.execute(selection)
    departement = result.scalars().one()
    nom_departement = departement.nom
    return nom_departement


# UPDATE


def update_collaborateur(idCollaborateur, aModifier, nouvelleValeur):
    session = create_session()

    match aModifier:
        case "login":
            stmt = update(Client).where(Client.id == idCollaborateur).values(nom_complet=nouvelleValeur)
        case "password":
            stmt = update(Client).where(Client.id == idCollaborateur).values(password=hash_password(nouvelleValeur))
        case "email":
            stmt = update(Client).where(Client.id == idCollaborateur).values(email=nouvelleValeur)
        case "departement_id":
            stmt = update(Client).where(Client.id == idCollaborateur).values(nom_entreprise=nouvelleValeur)
    try:
        session.execute(stmt)
        session.commit()
    finally:
        session.close()


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


def delete_collaborateur(loginCollaborateur):
    session = create_session()
    stmt = delete(Collaborateur).where(Collaborateur.login == loginCollaborateur)
    try:
        session.execute(stmt)
        session.commit()
    finally:
        session.close()


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
