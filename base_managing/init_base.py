from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base_managing.models import Base, Departement


# Configuration pour créer les données de base
def init_data(session):
    """Initialise les données de base dans la DB"""

    # Départements
    departements_data = [
        ("Commercial"),
        ("Support"),
        ("Gestion")
    ]

    for nom in departements_data:
        if not session.query(Departement).filter_by(nom=nom).first():
            dept = Departement(nom=nom)
            session.add(dept)

    session.commit()


def init_base():
    import os
    pwd = os.getenv("sql_epicevents")

    # Configuration de la base de données
    username = "epicevents"
    password = quote(pwd)  # encode les caractères spéciaux
    host = "localhost"
    port = 3306
    dbname = "epicevents"

    DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}"

    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Initialiser les données de base
    with SessionLocal() as session:
        init_data(session)


# initialisation des tables
init_base()
