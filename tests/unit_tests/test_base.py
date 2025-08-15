import pytest
from unittest.mock import Mock, patch
from sqlalchemy.exc import NoResultFound
from datetime import datetime

# Import du module à tester
import base_managing.CRUD as db_module
from base_managing.models import Collaborateur, Client, Contrat, Evenement


class TestCreateSession:
    """Tests pour la fonction create_session"""

    @patch('base_managing.CRUD.os.getenv')
    @patch('base_managing.CRUD.create_engine')
    @patch('base_managing.CRUD.sessionmaker')
    def test_create_session_success(self, mock_sessionmaker, mock_create_engine, mock_getenv):
        # Arrange
        mock_getenv.return_value = "test_password"
        mock_session = Mock()
        mock_sessionmaker.return_value.return_value.__enter__.return_value = mock_session

        # Action
        result = db_module.create_session()

        # Assert
        mock_getenv.assert_called_once_with("sql_epicevents")
        mock_create_engine.assert_called_once()
        assert result == mock_session


class TestAddFunctions:
    """Tests pour les fonctions d'ajout (CREATE)"""

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.hash_password')
    def test_add_collaborateur_success(self, mock_hash_password, mock_create_session):
        # Mocks
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_hash_password.return_value = "hashed_password"

        collaborateur = Mock()
        collaborateur.password = "plain_password"

        # Action
        db_module.add_collaborateur(collaborateur)

        # Assert
        mock_hash_password.assert_called_once_with("plain_password")
        assert collaborateur.password == "hashed_password"
        mock_session.add.assert_called_once_with(collaborateur)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.hash_password')
    @patch('base_managing.CRUD.capture_exception')
    def test_add_collaborateur_exception(self, mock_capture_exception, mock_hash_password, mock_create_session):
        # Mocks
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_session.commit.side_effect = Exception("Database error")

        collaborateur = Mock()
        collaborateur.password = "plain_password"

        # Act & Assert
        with pytest.raises(Exception):
            db_module.add_collaborateur(collaborateur)

        mock_session.rollback.assert_called_once()
        mock_capture_exception.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('base_managing.CRUD.create_session')
    def test_add_client_success(self, mock_create_session):
        # Mock
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        client = Mock()

        # Action
        db_module.add_client(client)

        # Assert
        mock_session.add.assert_called_once_with(client)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('base_managing.CRUD.create_session')
    def test_add_contrat_success(self, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        contrat = Mock()

        # Act
        db_module.add_contrat(contrat)

        # Assert
        mock_session.add.assert_called_once_with(contrat)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('base_managing.CRUD.create_session')
    def test_add_evenement_success(self, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        evenement = Mock()

        # Act
        db_module.add_evenement(evenement)

        # Assert
        mock_session.add.assert_called_once_with(evenement)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()


class TestReadFunctions:
    """Tests pour les fonctions de lecture (READ)"""

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.select')
    def test_get_all_collaborateurs_success(self, mock_select, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_result = Mock()
        mock_collaborateurs = [Mock(), Mock()]
        mock_result.scalars.return_value.all.return_value = mock_collaborateurs
        mock_session.execute.return_value = mock_result

        # Act
        result = db_module.get_all_collaborateurs()

        # Assert
        mock_select.assert_called_once_with(Collaborateur)
        mock_session.execute.assert_called_once()
        assert result == mock_collaborateurs

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.select')
    def test_get_all_clients_success(self, mock_select, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_result = Mock()
        mock_clients = [Mock(), Mock()]
        mock_result.scalars.return_value.all.return_value = mock_clients
        mock_session.execute.return_value = mock_result

        # Act
        result = db_module.get_all_clients()

        # Assert
        mock_select.assert_called_once_with(Client)
        mock_session.execute.assert_called_once()
        mock_session.close.assert_called_once()
        assert result == mock_clients

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.select')
    def test_get_collaborateur_by_id_success(self, mock_select, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_result = Mock()
        mock_collaborateur = Mock()
        mock_result.scalars.return_value.one.return_value = mock_collaborateur
        mock_session.execute.return_value = mock_result

        # Act
        result = db_module.get_collaborateur_by_id(1)

        # Assert
        mock_session.execute.assert_called_once()
        mock_session.close.assert_called_once()
        assert result == mock_collaborateur

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.select')
    @patch('builtins.print')
    def test_get_collaborateur_by_id_not_found(self, mock_print, mock_select, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_result = Mock()
        mock_result.scalars.return_value.one.side_effect = NoResultFound()
        mock_session.execute.return_value = mock_result

        # Act
        result = db_module.get_collaborateur_by_id(999)

        # Assert
        mock_print.assert_called_once_with("collaborateur non trouvé")
        mock_session.close.assert_called_once()
        assert result is False

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.select')
    def test_get_collaborateur_by_login_success(self, mock_select, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_result = Mock()
        mock_collaborateur = Mock()
        mock_result.scalars.return_value.one.return_value = mock_collaborateur
        mock_session.execute.return_value = mock_result

        # Act
        result = db_module.get_collaborateur_by_login("test_login")

        # Assert
        mock_session.execute.assert_called_once()
        mock_session.close.assert_called_once()
        assert result == mock_collaborateur

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.select')
    def test_get_clients_by_idCommercial(self, mock_select, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_result = Mock()
        mock_clients = [Mock(), Mock()]
        mock_result.scalars.return_value.all.return_value = mock_clients
        mock_session.execute.return_value = mock_result

        # Act
        result = db_module.get_clients_by_idCommercial(1)

        # Assert
        mock_session.execute.assert_called_once()
        assert result == mock_clients

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.select')
    def test_get_contrats_by_idCommercial(self, mock_select, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_result = Mock()
        mock_contrats = [Mock(), Mock()]
        mock_result.scalars.return_value.all.return_value = mock_contrats
        mock_session.execute.return_value = mock_result

        # Act
        result = db_module.get_contrats_by_idCommercial(42)

        # Assert
        mock_session.execute.assert_called_once()
        mock_select.assert_called_once()  # on s'assure que select() est bien utilisé
        assert result == mock_contrats

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.select')
    def test_get_contrat_by_id(self, mock_select, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_result = Mock()
        mock_contrat = Mock()
        mock_result.scalars.return_value.one.return_value = mock_contrat
        mock_session.execute.return_value = mock_result

        # Act
        result = db_module.get_contrat_by_id(5)

        # Assert
        mock_session.execute.assert_called_once()
        mock_select.assert_called_once()
        assert result == mock_contrat

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.select')
    def test_get_evenements_without_support(self, mock_select, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_result = Mock()
        mock_evenements = [Mock(), Mock()]
        mock_result.scalars.return_value.all.return_value = mock_evenements
        mock_session.execute.return_value = mock_result

        # Act
        result = db_module.get_evenements_without_support()

        # Assert
        mock_session.execute.assert_called_once()
        assert result == mock_evenements

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.select')
    def test_get_nom_departement_by_id(self, mock_select, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_result = Mock()
        mock_departement = Mock()
        mock_departement.nom = "Test Department"
        mock_result.scalars.return_value.one.return_value = mock_departement
        mock_session.execute.return_value = mock_result

        # Act
        result = db_module.get_nom_departement_by_id(1)

        # Assert
        mock_session.execute.assert_called_once()
        assert result == "Test Department"


class TestUpdateFunctions:
    """Tests pour les fonctions de mise à jour (UPDATE)"""

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.update')
    def test_update_client_nom_complet(self, mock_update, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_stmt = Mock()
        mock_update.return_value.where.return_value.values.return_value = mock_stmt

        # Act
        db_module.update_client(1, "nom_complet", "Nouveau Nom")

        # Assert
        mock_session.execute.assert_called_once_with(mock_stmt)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.update')
    def test_update_client_email(self, mock_update, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_stmt = Mock()
        mock_update.return_value.where.return_value.values.return_value = mock_stmt

        # Act
        db_module.update_client(1, "email", "nouveau@email.com")

        # Assert
        mock_session.execute.assert_called_once_with(mock_stmt)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.update')
    @patch('base_managing.CRUD.capture_exception')
    def test_update_client_exception(self, mock_capture_exception, mock_update, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_session.execute.side_effect = Exception("Database error")

        # Act & Assert
        with pytest.raises(Exception):
            db_module.update_client(1, "nom_complet", "Nouveau Nom")

        mock_session.rollback.assert_called_once()
        mock_capture_exception.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.update')
    def test_update_evenement_nom(self, mock_update, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_stmt = Mock()
        mock_update.return_value.where.return_value.values.return_value = mock_stmt

        # Act
        db_module.update_evenement(1, "nom", "Nouveau Nom Event")

        # Assert
        mock_session.execute.assert_called_once_with(mock_stmt)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.update')
    def test_update_evenement_responsable_support_id(self, mock_update, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_stmt = Mock()
        mock_update.return_value.where.return_value.values.return_value = mock_stmt

        # Act
        db_module.update_evenement(1, "responsable_support_id", 5)

        # Assert
        mock_session.execute.assert_called_once_with(mock_stmt)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()


class TestDeleteFunctions:
    """Tests pour les fonctions de suppression (DELETE)"""

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.delete')
    def test_delete_collaborateur_success(self, mock_delete, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_stmt = Mock()
        mock_delete.return_value.where.return_value = mock_stmt

        # Act
        db_module.delete_collaborateur(1)

        # Assert
        mock_delete.assert_called_once_with(Collaborateur)
        mock_session.execute.assert_called_once_with(mock_stmt)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.delete')
    def test_delete_client_success(self, mock_delete, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_stmt = Mock()
        mock_delete.return_value.where.return_value = mock_stmt

        # Act
        db_module.delete_client(1)

        # Assert
        mock_delete.assert_called_once_with(Client)
        mock_session.execute.assert_called_once_with(mock_stmt)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.delete')
    @patch('base_managing.CRUD.capture_exception')
    def test_delete_contrat_exception(self, mock_capture_exception, mock_delete, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_session.execute.side_effect = Exception("Database error")

        # Act & Assert
        with pytest.raises(Exception):
            db_module.delete_contrat(1)

        mock_session.rollback.assert_called_once()
        mock_capture_exception.assert_called_once()
        mock_session.close.assert_called_once()

    @patch('base_managing.CRUD.create_session')
    @patch('base_managing.CRUD.delete')
    def test_delete_evenement_success(self, mock_delete, mock_create_session):
        # Arrange
        mock_session = Mock()
        mock_create_session.return_value = mock_session
        mock_stmt = Mock()
        mock_delete.return_value.where.return_value = mock_stmt

        # Act
        db_module.delete_evenement(1)

        # Assert
        mock_delete.assert_called_once_with(Evenement)
        mock_session.execute.assert_called_once_with(mock_stmt)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()


# Fixtures utiles pour les tests
@pytest.fixture
def sample_collaborateur():
    """Fixture pour créer un collaborateur de test"""
    collaborateur = Mock(spec=Collaborateur)
    collaborateur.id = 1
    collaborateur.login = "test_user"
    collaborateur.password = "test_password"
    collaborateur.email = "test@example.com"
    collaborateur.departement_id = 1
    return collaborateur


@pytest.fixture
def sample_client():
    """Fixture pour créer un client de test"""
    client = Mock(spec=Client)
    client.id = 1
    client.nom_complet = "Test Client"
    client.email = "client@example.com"
    client.telephone = "0123456789"
    client.nom_entreprise = "Test Company"
    client.commercial_id = 1
    return client


@pytest.fixture
def sample_contrat():
    """Fixture pour créer un contrat de test"""
    contrat = Mock(spec=Contrat)
    contrat.id = 1
    contrat.client_id = 1
    contrat.commercial_id = 1
    contrat.montant_total = 10000.0
    contrat.montant_restant = 5000.0
    contrat.statut_id = 1
    contrat.date_signature = datetime.now()
    contrat.date_fin_prevue = datetime.now()
    return contrat


@pytest.fixture
def sample_evenement():
    """Fixture pour créer un événement de test"""
    evenement = Mock(spec=Evenement)
    evenement.id = 1
    evenement.nom = "Test Event"
    evenement.contrat_id = 1
    evenement.responsable_support_id = 1
    evenement.date_debut = datetime.now()
    evenement.date_fin = datetime.now()
    evenement.lieu = "Test Location"
    evenement.adresse_lieu = "123 Test Street"
    evenement.nombre_participants = 50
    evenement.statut_id = 1
    evenement.notes = "Test notes"
    return evenement


if __name__ == "__main__":
    pytest.main([__file__])
