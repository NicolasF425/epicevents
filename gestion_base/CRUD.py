from init_session import create_session
from sqlalchemy import select, update, delete
from initialisation_base import Client, Contrat, Evenement


# CREATE


def add_collaborateur(collaborateur):
    try:
        session = create_session()
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
    client = result.one()
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


# DELETE


def delete_client(idClient):
    session = create_session()
    stmt = delete(Client).where(Client.id == idClient)
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


def delete_contrat(idContrat):
    session = create_session()
    stmt = delete(Contrat).where(Contrat.id == idContrat)
    try:
        session.execute(stmt)
        session.commit()
    finally:
        session.close()
