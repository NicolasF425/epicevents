# -*- coding: utf-8 -*-
from datetime import date
from sqlalchemy import (
    Column, Integer, String, Text, DateTime, Date,
    DECIMAL, ForeignKey, CheckConstraint, Index
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func


Base = declarative_base()


class Departement(Base):
    """Table des départements de l'entreprise"""
    __tablename__ = 'departements'

    id = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False, unique=True)

    # Relation vers les collaborateurs
    collaborateurs = relationship("Collaborateur", back_populates="departement")

    def __repr__(self):
        return f"<Departement(nom='{self.nom}')>"


class Collaborateur(Base):
    """Table des collaborateurs Epic Events"""
    __tablename__ = 'collaborateurs'

    id = Column(Integer, primary_key=True)
    login = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    departement_id = Column(Integer, ForeignKey('departements.id'), nullable=False)

    # Relations
    departement = relationship("Departement", back_populates="collaborateurs")
    clients_geres = relationship("Client", back_populates="commercial")
    contrats_commercial = relationship("Contrat", foreign_keys="Contrat.commercial_id", back_populates="commercial")
    evenements_responsable = relationship("Evenement", back_populates="responsable_support")

    # Index
    __table_args__ = (
        Index('idx_collaborateur_login', 'login'),
        Index('idx_collaborateur_departement', 'departement_id'),
    )

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("Email invalide")
        return email

    def __repr__(self):
        return f"<Collaborateur(login='{self.login}', departement='{self.departement.nom}')>"


class Client(Base):
    """Table des clients Epic Events"""
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    nom_complet = Column(String(200), nullable=False)
    email = Column(String(255), nullable=False)
    telephone = Column(String(20))
    nom_entreprise = Column(String(200), nullable=False)
    date_creation = Column(Date, nullable=False, default=date.today)
    date_maj = Column(DateTime, default=func.now(), onupdate=func.now())
    commercial_id = Column(Integer, ForeignKey('collaborateurs.id'), nullable=False)

    # Relations
    commercial = relationship("Collaborateur", back_populates="clients_geres")
    contrats = relationship("Contrat", back_populates="client")
    evenements = relationship("Evenement", back_populates="client")

    # Index
    __table_args__ = (
        Index('idx_client_commercial', 'commercial_id'),
    )

    def __repr__(self):
        return f"<Client(entreprise='{self.nom_entreprise}', contact='{self.contact_complet}')>"


class Contrat(Base):
    """Table des contrats clients"""
    __tablename__ = 'contrats'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    commercial_id = Column(Integer, ForeignKey('collaborateurs.id'), nullable=False)
    montant_total = Column(DECIMAL(10, 2), nullable=False)
    montant_restant = Column(DECIMAL(10, 2), nullable=False)
    date_creation = Column(Date, nullable=False, default=date.today)
    date_signature = Column(Date, nullable=True)

    # Relations
    client = relationship("Client", back_populates="contrats")
    commercial = relationship("Collaborateur", foreign_keys=[commercial_id], back_populates="contrats_commercial")
    evenements = relationship("Evenement", back_populates="contrat")

    # Contraintes et index
    __table_args__ = (
        CheckConstraint('montant_restant >= 0', name='chk_montant_restant_positif'),
        CheckConstraint('montant_restant <= montant_total', name='chk_montant_restant_coherent'),
        Index('idx_contrat_client', 'client_id'),
        Index('idx_contrat_commercial', 'commercial_id'),
        Index('idx_contrat_montant', 'montant_restant'),
    )

    @validates('montant_restant')
    def validate_montant_restant(self, key, montant):
        if montant < 0:
            raise ValueError("Le montant restant ne peut pas être négatif")
        if hasattr(self, 'montant_total') and montant > self.montant_total:
            raise ValueError("Le montant restant ne peut pas être supérieur au montant total")
        return montant

    @property
    def est_signe(self):
        return self.date_signature is not None

    @property
    def est_paye_integralement(self):
        return self.montant_restant == 0

    def __repr__(self):
        return f"<Contrat(numero='{self.numero_contrat}', client='{self.client.nom_entreprise}')>"


class Evenement(Base):
    """Table des évènements"""
    __tablename__ = 'evenements'

    id = Column(Integer, primary_key=True)
    nom = Column(String(200), nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    contrat_id = Column(Integer, ForeignKey('contrats.id'), nullable=False)
    responsable_support_id = Column(Integer, ForeignKey('collaborateurs.id'), nullable=True)
    date_debut = Column(DateTime, nullable=False)
    date_fin = Column(DateTime, nullable=False)
    lieu = Column(String(300))
    adresse_lieu = Column(Text)
    nombre_participants = Column(Integer)
    notes = Column(Text)
    date_creation = Column(DateTime, default=func.now())
    derniere_maj = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relations
    client = relationship("Client", back_populates="evenements")
    contrat = relationship("Contrat", back_populates="evenements")
    responsable_support = relationship("Collaborateur", back_populates="evenements_responsable")

    # Contraintes et index
    __table_args__ = (
        CheckConstraint('date_fin > date_debut', name='chk_dates_evenement_coherentes'),
        Index('idx_evenement_contrat', 'contrat_id'),
        Index('idx_evenement_responsable', 'responsable_support_id'),
        Index('idx_evenement_dates', 'date_debut', 'date_fin'),
        Index('idx_evenement_periode', 'date_debut', 'date_fin'),
    )

    @validates('date_fin')
    def validate_dates(self, key, date_fin):
        if hasattr(self, 'date_debut') and self.date_debut and date_fin <= self.date_debut:
            raise ValueError("La date de fin doit être postérieure à la date de début")
        return date_fin

    @property
    def duree_jours(self):
        if self.date_debut and self.date_fin:
            return (self.date_fin.date() - self.date_debut.date()).days
        return 0

    def __repr__(self):
        return f"<Evenement(nom='{self.nom}', date_debut='{self.date_debut}')>"


'''
class HistoriqueModification(Base):
    """Table d'audit pour tracer les modifications"""
    __tablename__ = 'historique_modifications'

    id = Column(Integer, primary_key=True)
    table_name = Column(String(50), nullable=False)
    record_id = Column(Integer, nullable=False)
    action = Column(String(20), nullable=False)  # INSERT, UPDATE, DELETE
    ancien_valeur = Column(Text)  # JSON serialized
    nouvelle_valeur = Column(Text)  # JSON serialized
    utilisateur_id = Column(Integer, ForeignKey('collaborateurs.id'))
    date_modification = Column(DateTime, default=func.now())

    # Relation
    utilisateur = relationship("Collaborateur", back_populates="modifications")

    # Index
    __table_args__ = (
        Index('idx_historique_table_record', 'table_name', 'record_id'),
        Index('idx_historique_date', 'date_modification'),
    )

    def __repr__(self):
        return f"<HistoriqueModification(table='{self.table_name}', action='{self.action}')>"
'''
