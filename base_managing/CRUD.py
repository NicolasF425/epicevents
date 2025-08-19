from sqlalchemy import select, update, delete
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import NoResultFound
from base_managing.models import Collaborateur, Client, Contrat, Evenement, Departement
from utilities.gestion_hashage import hash_password
from sentry_sdk import capture_exception
import os


Base = declarative_base()


def create_session():
    from dotenv import load_dotenv
    load_dotenv()
    pwd = os.getenv("sql_epicevents")

    # Configuration de la base de données
    username = "epicevents"
    password = quote(pwd)  # encode les caractères spéciaux
    host = "localhost"
    port = 3306
    dbname = "epicevents"

    DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}"

    engine = create_engine(DATABASE_URL, echo=False)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    with SessionLocal() as session:
        return session


# CREATE (add)


def add_collaborateur(collaborateur):
    try:
        session = create_session()
        collaborateur.password = hash_password(collaborateur.password)
        session.add(collaborateur)
        session.commit()
    except Exception as e:
        session.rollback()
        capture_exception(e)  # Envoie l'erreur à Sentry
        raise  # Pour que l'erreur ne soit pas silencieuse
    finally:
        session.close()


def add_client(client):
    try:
        session = create_session()
        session.add(client)
        session.commit()
    except Exception as e:
        session.rollback()
        capture_exception(e)
        raise
    finally:
        session.close()


def add_contrat(contrat):
    try:
        session = create_session()
        session.add(contrat)
        session.commit()
    except Exception as e:
        session.rollback()
        capture_exception(e)
        raise
    finally:
        session.close()


def add_evenement(evenement):
    try:
        session = create_session()
        session.add(evenement)
        session.commit()
    except Exception as e:
        session.rollback()
        capture_exception(e)
        raise
    finally:
        session.close()


# READ (get)


def get_all_collaborateurs():
    try:
        session = create_session()
        selection = select(Collaborateur)
        result = session.execute(selection)
        all_collaborateurs = result.scalars().all()
        return all_collaborateurs
    finally:
        session.close()


def get_all_clients():
    try:
        session = create_session()
        selection = select(Client)
        result = session.execute(selection)
        all_clients = result.scalars().all()
        return all_clients
    finally:
        if session:
            session.close()


def get_all_contrats():
    try:
        session = create_session()
        selection = select(Contrat)
        result = session.execute(selection)
        all_contrats = result.scalars().all()
        return all_contrats
    finally:
        if session:
            session.close()


def get_all_evenements():
    try:
        session = create_session()
        selection = select(Evenement)
        result = session.execute(selection)
        all_evenements = result.scalars().all()
        return all_evenements
    finally:
        if session:
            session.close()


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


def get_collaborateurs_by_idDepartement(idDepartement):
    try:
        session = create_session()
        selection = select(Collaborateur).where(Collaborateur.departement_id == idDepartement)
        result = session.execute(selection)
        collaborateur = result.scalars().all()
        return collaborateur
    except NoResultFound:
        print("Aucun collaborateur trouvé")
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
    try:
        session = create_session()
        selection = select(Client).where(Client.id == idClient)
        result = session.execute(selection)
        client = result.scalars().one()
        return client
    finally:
        session.close()


def get_clients_by_idCommercial(idCollab):
    try:
        session = create_session()
        selection = select(Client).where(Client.commercial_id == idCollab)
        result = session.execute(selection)
        clients = result.scalars().all()
        return clients
    finally:
        session.close()


def get_contrats_by_idCommercial(idCollab):
    try:
        session = create_session()
        selection = select(Contrat).where(Contrat.commercial_id == idCollab)
        result = session.execute(selection)
        contrats = result.scalars().all()
        return contrats
    finally:
        session.close()


def get_contrat_by_id(idContrat):
    try:
        session = create_session()
        selection = select(Contrat).where(Contrat.id == idContrat)
        result = session.execute(selection)
        contrat = result.scalars().one()
        return contrat
    finally:
        session.close()


def get_evenements_by_idSupport(idCollaborateur):
    try:
        session = create_session()
        selection = select(Evenement).where(Evenement.responsable_support_id == idCollaborateur)
        result = session.execute(selection)
        evenements = result.scalars().all()
        return evenements
    finally:
        session.close()


def get_evenements_without_support():
    try:
        session = create_session()
        selection = select(Evenement).where(Evenement.responsable_support_id.is_(None))
        result = session.execute(selection)
        evenements = result.scalars().all()
        return evenements
    finally:
        session.close()


def get_evenement_by_id(id):
    try:
        session = create_session()
        selection = select(Evenement).where(Evenement.id == id)
        result = session.execute(selection)
        evenement = result.scalars().one()
        return evenement
    finally:
        session.close()


def get_nom_departement_by_id(idDepartement):
    try:
        session = create_session()
        selection = select(Departement).where(Departement.id == idDepartement)
        result = session.execute(selection)
        departement = result.scalars().one()
        nom_departement = departement.nom
        return nom_departement
    finally:
        session.close()


# UPDATE


def update_collaborateur(idCollaborateur, aModifier, nouvelleValeur):

    session = create_session()

    match aModifier:
        case "login":
            stmt = update(Collaborateur).where(Collaborateur.id == idCollaborateur) \
                .values(login=nouvelleValeur)
        case "password":
            stmt = update(Collaborateur).where(Collaborateur.id == idCollaborateur) \
                .values(password=hash_password(nouvelleValeur))
        case "email":
            stmt = update(Collaborateur).where(Collaborateur.id == idCollaborateur) \
                .values(email=nouvelleValeur)
        case "departement_id":
            stmt = update(Collaborateur).where(Collaborateur.departement_id == idCollaborateur) \
                .values(departement_id=nouvelleValeur)
    try:
        session.execute(stmt)
        session.commit()
    except Exception as e:
        session.rollback()
        capture_exception(e)
        raise
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
    except Exception as e:
        session.rollback()
        capture_exception(e)
        raise
    finally:
        session.close()


def update_contrat(idContrat, aModifier, nouvelleValeur):
    session = create_session()

    match aModifier:
        case "client_id":
            stmt = update(Contrat).where(Contrat.id == idContrat).values(client_id=nouvelleValeur)
        case "commercial_id":
            stmt = update(Contrat).where(Contrat.id == idContrat).values(commercial_id=nouvelleValeur)
        case "montant_total":
            stmt = update(Contrat).where(Contrat.id == idContrat).values(montant_total=nouvelleValeur)
        case "montant_restant":
            stmt = update(Contrat).where(Contrat.id == idContrat).values(montant_restant=nouvelleValeur)
        case "est_signe":
            stmt = update(Contrat).where(Contrat.id == idContrat).values(est_signe=nouvelleValeur)
    try:
        session.execute(stmt)
        session.commit()
    except Exception as e:
        session.rollback()
        capture_exception(e)
        raise
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
        case "notes":
            stmt = update(Evenement).where(Evenement.id == idEvenement).values(notes=nouvelleValeur)
    try:
        session.execute(stmt)
        session.commit()
    except Exception as e:
        session.rollback()
        capture_exception(e)
        raise
    finally:
        session.close()


# DELETE


def delete_collaborateur(idCollaborateur):
    session = create_session()
    stmt = delete(Collaborateur).where(Collaborateur.id == idCollaborateur)
    try:
        session.execute(stmt)
        session.commit()
    except Exception as e:
        session.rollback()
        capture_exception(e)
        raise
    finally:
        session.close()


def delete_client(idClient):
    session = create_session()
    stmt = delete(Client).where(Client.id == idClient)
    try:
        session.execute(stmt)
        session.commit()
    except Exception as e:
        session.rollback()
        capture_exception(e)
        raise
    finally:
        session.close()


def delete_contrat(idContrat):
    session = create_session()
    stmt = delete(Contrat).where(Contrat.id == idContrat)
    try:
        session.execute(stmt)
        session.commit()
    except Exception as e:
        session.rollback()
        capture_exception(e)
        raise
    finally:
        session.close()


def delete_evenement(idEvenement):
    session = create_session()
    stmt = delete(Evenement).where(Evenement.id == idEvenement)
    try:
        session.execute(stmt)
        session.commit()
    except Exception as e:
        session.rollback()
        capture_exception(e)
        raise
    finally:
        session.close()
