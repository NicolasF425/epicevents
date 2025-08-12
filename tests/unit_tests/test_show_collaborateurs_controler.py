from unittest.mock import patch, MagicMock
from controlers.show_collaborateurs_controler import ShowCollaborateursControler


@patch("controlers.show_collaborateurs_controler.get_collaborateur_by_id", return_value="fake_collab")
@patch("controlers.show_collaborateurs_controler.ShowCollaborateursControler.check_token_validity",
       return_value={"id": 42})
@patch("controlers.show_collaborateurs_controler.ShowSingleCollaborateurView")
def test_select_action_2(mock_view_cls, mock_token, mock_get_collab):
    mock_view = MagicMock()
    mock_view_cls.return_value = mock_view

    ctrl = ShowCollaborateursControler()
    ctrl.select_action("2", 1)

    mock_get_collab.assert_called_with(1)
    mock_view.display_single_collaborateur.assert_called_with("fake_collab")
