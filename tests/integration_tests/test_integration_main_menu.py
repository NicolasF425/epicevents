from unittest.mock import Mock, patch
from views.main_menu_view import MainMenuView
from utilities.constantes import GESTION


# Tests d'intégration
class TestMainMenuIntegration:
    """Tests d'intégration entre la vue et le contrôleur"""

    @patch('views.main_menu_view.clear_screen')  # Chemin complet
    @patch('builtins.input', return_value='1')
    @patch('controlers.main_menu_controler.ShowCollaborateursView')
    def test_full_workflow_gestion_user(self, mock_view_class, mock_input, mock_clear):
        """Test du workflow complet pour un utilisateur gestion"""
        mock_view_instance = Mock()
        mock_view_class.return_value = mock_view_instance

        # Créer une instance de la vue
        view = MainMenuView()
        # Réinitialiser les variables de classe
        view.num = 0
        view.mapping = {}

        # Mock du token
        with patch.object(view, 'check_token_validity', return_value={"departement_id": GESTION}):
            view.display_items()

        # Vérifier que la bonne vue a été appelée
        mock_view_class.assert_called_once()
        mock_view_instance.display_collaborateurs.assert_called_once()
