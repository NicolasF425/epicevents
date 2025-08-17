import pytest
from unittest.mock import Mock, patch

# Import des classes à tester
from views.main_menu_view import MainMenuView
from controlers.main_menu_controler import MainMenuControler

# Import des constantes (vous devrez peut-être ajuster ces imports selon votre structure)
from utilities.constantes import COMMERCIAL, GESTION, SUPPORT
from utilities.constantes import COMMERCIAL_COLOR, SUPPORT_COLOR, RESET


class TestMainMenuView:
    """Tests pour la classe MainMenuView"""

    @pytest.fixture
    def view(self):
        """Fixture pour créer une instance de MainMenuView"""
        view = MainMenuView()
        # Réinitialiser les variables de classe pour chaque test
        view.num = 0
        view.mapping = {}
        return view

    @pytest.fixture
    def mock_token_gestion(self):
        """Token fictif pour un utilisateur du département gestion"""
        return {"departement_id": GESTION}

    @pytest.fixture
    def mock_token_commercial(self):
        """Token fictif pour un utilisateur du département commercial"""
        return {"departement_id": COMMERCIAL}

    @pytest.fixture
    def mock_token_support(self):
        """Token fictif pour un utilisateur du département support"""
        return {"departement_id": SUPPORT}

    def test_build_menu_gestion_user(self, view, mock_token_gestion):
        """Test de build_menu pour un utilisateur du département gestion"""
        with patch.object(view, 'check_token_validity', return_value=mock_token_gestion):
            view.build_menu()

            # Vérifier que les bonnes actions sont mappées
            assert "manage_collaborateur" in view.mapping
            assert "add_support_evenement" in view.mapping
            assert "show_clients" in view.mapping
            assert "show_contrats" in view.mapping
            assert "show_evenements" in view.mapping
            assert "quitter" in view.mapping

            # Vérifier que les actions spécifiques aux autres départements ne sont pas présentes
            assert "my_clients" not in view.mapping
            assert "my_contrats" not in view.mapping
            assert "my_evenements" not in view.mapping

    def test_build_menu_commercial_user(self, view, mock_token_commercial):
        """Test de build_menu pour un utilisateur du département commercial"""
        with patch.object(view, 'check_token_validity', return_value=mock_token_commercial):
            view.build_menu()

            # Vérifier que les bonnes actions sont mappées
            assert "my_clients" in view.mapping
            assert "my_contrats" in view.mapping
            assert "show_clients" in view.mapping
            assert "show_contrats" in view.mapping
            assert "show_evenements" in view.mapping
            assert "quitter" in view.mapping

            # Vérifier que les actions spécifiques aux autres départements ne sont pas présentes
            assert "manage_collaborateur" not in view.mapping
            assert "add_support_evenement" not in view.mapping
            assert "my_evenements" not in view.mapping

            # Vérifier le nombre total d'items
            assert len(view.mapping) == 6

    def test_build_menu_support_user(self, view, mock_token_support):
        """Test de build_menu pour un utilisateur du département support"""
        with patch.object(view, 'check_token_validity', return_value=mock_token_support):
            view.build_menu()

            # Vérifier que les bonnes actions sont mappées
            assert "my_evenements" in view.mapping
            assert "show_clients" in view.mapping
            assert "show_contrats" in view.mapping
            assert "show_evenements" in view.mapping
            assert "quitter" in view.mapping

            # Vérifier que les actions spécifiques aux autres départements ne sont pas présentes
            assert "manage_collaborateur" not in view.mapping
            assert "add_support_evenement" not in view.mapping
            assert "my_clients" not in view.mapping
            assert "my_contrats" not in view.mapping

            # Vérifier le nombre total d'items
            assert len(view.mapping) == 5

    def test_build_menu_invalid_token(self, view, capsys):
        """Test de build_menu avec un token invalide"""
        with patch.object(view, 'check_token_validity', return_value=False):
            view.build_menu()

            # Vérifier que le message d'erreur est affiché
            captured = capsys.readouterr()
            assert "Erreur de token" in captured.out

            # Vérifier que le mapping est vide (pas de nouvelles entrées ajoutées)
            assert len(view.mapping) == 0
            # Vérifier que num n'a pas été incrémenté
            assert view.num == 0

    @patch('builtins.print')
    def test_item_methods_output(self, mock_print, view):
        """Test des méthodes d'affichage des items"""
        # Test item_manage_collaborateur
        view.item_manage_collaborateur(1)
        mock_print.assert_called_with(f"{SUPPORT_COLOR}1) Gérer les collaborateurs{RESET}")

        # Test item_my_clients
        view.item_my_clients(2)
        mock_print.assert_called_with(f"{COMMERCIAL_COLOR}2) Mes clients{RESET}")

        # Test item_show_clients
        view.item_show_clients(3)
        mock_print.assert_called_with("3) Lister les clients")

    @patch('views.main_menu_view.clear_screen')  # Chemin complet vers clear_screen
    @patch('builtins.input', return_value='1')
    @patch('builtins.print')
    def test_display_items_interaction(self, mock_print, mock_input, mock_clear, view, mock_token_gestion):
        """Test de display_items avec interaction utilisateur"""
        with patch.object(view, 'check_token_validity', return_value=mock_token_gestion):
            with patch.object(view.controler, 'select_action') as mock_select_action:
                view.display_items()

                # Vérifier que clear_screen a été appelé
                mock_clear.assert_called_once()

                # Vérifier que le contrôleur a été appelé avec les bons paramètres
                mock_select_action.assert_called_once_with(1, view.mapping)

    @patch('views.main_menu_view.clear_screen')  # Chemin complet vers clear_screen
    @patch('builtins.input', return_value='999')  # Numéro invalide
    @patch.object(MainMenuView, 'check_token_validity')
    def test_display_items_invalid_input(self, mock_token, mock_input, mock_clear, view):
        """Test avec un numéro d'action invalide"""
        mock_token.return_value = {"departement_id": GESTION}

        with patch.object(view.controler, 'select_action') as mock_select_action:
            view.display_items()

            # Le contrôleur ne devrait pas être appelé avec un numéro invalide
            mock_select_action.assert_not_called()


class TestMainMenuControler:
    """Tests pour la classe MainMenuControler"""

    @pytest.fixture
    def controler(self):
        """Fixture pour créer une instance de MainMenuControler"""
        return MainMenuControler()

    @pytest.fixture
    def sample_mapping(self):
        """Mapping fictif pour les tests"""
        return {
            "manage_collaborateur": 1,
            "my_clients": 2,
            "show_clients": 3,
            "quitter": 4
        }

    @patch('controlers.main_menu_controler.ShowCollaborateursView')
    def test_select_action_manage_collaborateur(self, mock_view_class, controler, sample_mapping):
        """Test de select_action pour manage_collaborateur"""
        mock_view_instance = Mock()
        mock_view_class.return_value = mock_view_instance

        controler.select_action(1, sample_mapping)

        # Vérifier que la vue a été créée et la méthode appelée
        mock_view_class.assert_called_once()
        mock_view_instance.display_collaborateurs.assert_called_once()

    @patch('controlers.main_menu_controler.ShowClientsView')
    def test_select_action_my_clients(self, mock_view_class, controler, sample_mapping):
        """Test de select_action pour my_clients"""
        mock_view_instance = Mock()
        mock_view_class.return_value = mock_view_instance

        controler.select_action(2, sample_mapping)

        # Vérifier que la vue a été créée et la méthode appelée avec le bon paramètre
        mock_view_class.assert_called_once()
        mock_view_instance.display_clients.assert_called_once_with(True)

    @patch('controlers.main_menu_controler.ShowClientsView')
    def test_select_action_show_clients(self, mock_view_class, controler, sample_mapping):
        """Test de select_action pour show_clients"""
        mock_view_instance = Mock()
        mock_view_class.return_value = mock_view_instance

        controler.select_action(3, sample_mapping)

        # Vérifier que la vue a été créée et la méthode appelée sans paramètre
        mock_view_class.assert_called_once()
        mock_view_instance.display_clients.assert_called_once_with()

    @patch('controlers.main_menu_controler.ShowContratsView')
    def test_select_action_my_contrats(self, mock_view_class, controler):
        """Test de select_action pour my_contrats"""
        mock_view_instance = Mock()
        mock_view_class.return_value = mock_view_instance
        mapping = {"my_contrats": 1}

        controler.select_action(1, mapping)

        mock_view_class.assert_called_once()
        mock_view_instance.display_contrats.assert_called_once_with(True)

    @patch('controlers.main_menu_controler.ShowContratsView')
    def test_select_action_show_contrats(self, mock_view_class, controler):
        """Test de select_action pour show_contrats"""
        mock_view_instance = Mock()
        mock_view_class.return_value = mock_view_instance
        mapping = {"show_contrats": 1}

        controler.select_action(1, mapping)

        mock_view_class.assert_called_once()
        mock_view_instance.display_contrats.assert_called_once_with()

    @patch('controlers.main_menu_controler.ShowEvenementsView')
    def test_select_action_add_support_evenement(self, mock_view_class, controler):
        """Test de select_action pour add_support_evenement"""
        mock_view_instance = Mock()
        mock_view_class.return_value = mock_view_instance
        mapping = {"add_support_evenement": 1}

        controler.select_action(1, mapping)

        mock_view_class.assert_called_once()
        mock_view_instance.display_evenements.assert_called_once_with("evenements_sans_support")

    @patch('controlers.main_menu_controler.ShowEvenementsView')
    def test_select_action_my_evenements(self, mock_view_class, controler):
        """Test de select_action pour my_evenements"""
        mock_view_instance = Mock()
        mock_view_class.return_value = mock_view_instance
        mapping = {"my_evenements": 1}

        controler.select_action(1, mapping)

        mock_view_class.assert_called_once()
        mock_view_instance.display_evenements.assert_called_once_with("mes_evenements")

    @patch('controlers.main_menu_controler.ShowEvenementsView')
    def test_select_action_show_evenements(self, mock_view_class, controler):
        """Test de select_action pour show_evenements"""
        mock_view_instance = Mock()
        mock_view_class.return_value = mock_view_instance
        mapping = {"show_evenements": 1}

        controler.select_action(1, mapping)

        mock_view_class.assert_called_once()
        mock_view_instance.display_evenements.assert_called_once_with()

    def test_select_action_quitter(self, controler):
        """Test de select_action pour quitter (ne fait rien)"""
        mapping = {"quitter": 1}

        # Cette action ne devrait rien faire, donc pas d'exception
        try:
            controler.select_action(1, mapping)
            assert True  # Si on arrive ici, c'est que ça a fonctionné
        except Exception:
            pytest.fail("L'action quitter ne devrait pas lever d'exception")

    def test_select_action_invalid_number(self, controler, sample_mapping):
        """Test avec un numéro d'action qui n'existe pas dans le mapping"""
        # Aucune vue ne devrait être créée
        with patch('controlers.main_menu_controler.ShowClientsView') as mock_view:
            controler.select_action(999, sample_mapping)
            mock_view.assert_not_called()
