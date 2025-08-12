from unittest.mock import patch


@patch("views.show_collaborateurs_view.get_all_collaborateurs")
@patch("views.show_collaborateurs_view.get_nom_departement_by_id", return_value="Ventes")
@patch("views.show_collaborateurs_view.ShowCollaborateursView.check_token_validity", return_value={"id": 42})
@patch("views.show_collaborateurs_view.clear_screen")
@patch("views.show_collaborateurs_view.input", side_effect=["2", "1"])
def test_display_collaborateurs_affichage(mock_input, mock_clear, mock_token, mock_get_nom_dep, mock_get_all, capsys):
    mock_get_all.return_value = [
        type("FakeCollab", (), {
            "id": 1,
            "login": "jdupont",
            "email": "jean.dupont@example.com",
            "nom": "Dupont",
            "prenom": "Jean",
            "departement_id": 2
        })()
    ]

    from views.show_collaborateurs_view import ShowCollaborateursView
    view = ShowCollaborateursView()
    view.display_collaborateurs()

    captured = capsys.readouterr()
    assert "Dupont" in captured.out
    assert "jdupont" in captured.out
