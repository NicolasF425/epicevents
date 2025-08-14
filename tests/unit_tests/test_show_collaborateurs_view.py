from unittest.mock import patch


@patch("views.show_collaborateurs_view.get_all_collaborateurs")
@patch("views.show_collaborateurs_view.get_nom_departement_by_id", return_value="Ventes")
@patch("views.common_view.JWTManager.verify_token", return_value={"id": 42, "departement_id": 1})
@patch("views.show_collaborateurs_view.clear_screen")
@patch("controlers.show_collaborateurs_controler.ShowCollaborateursControler.select_action")  # Mock du contrôleur
@patch("builtins.input", return_value="")
def test_display_collaborateurs_affichage(mock_input, mock_controller, mock_clear, mock_jwt, mock_get_nom_dep,
                                          mock_get_all, capsys):
    fake_collab = type("FakeCollab", (), {
        "id": 1,
        "login": "Joe123",
        "email": "joe@epic-events.com",
        "departement_id": 1
    })()

    mock_get_all.return_value = [fake_collab]

    from views.show_collaborateurs_view import ShowCollaborateursView
    view = ShowCollaborateursView()
    view.display_collaborateurs()

    captured = capsys.readouterr()
    assert "Joe123" in captured.out
    assert "joe@epic-events.com" in captured.out
    assert "COLLABORATEURS" in captured.out
