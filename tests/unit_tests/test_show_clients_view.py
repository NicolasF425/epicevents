from unittest.mock import patch


@patch("views.show_clients_view.input", return_value="")  # <─ empêche la lecture réelle
@patch("views.show_clients_view.get_clients_by_idCommercial")
@patch("views.show_clients_view.ShowClientsView.check_token_validity", return_value={"id": 42})
@patch("views.show_clients_view.clear_screen")
def test_affichage_mes_clients(mock_clear, mock_token, mock_get_clients, mock_input, capsys):
    mock_get_clients.return_value = [
        type("FakeClient", (), {"id": 1, "nom_entreprise": "Test SA"})()
    ]

    from views.show_clients_view import ShowClientsView
    view = ShowClientsView()
    view.display_clients(filtered=True)

    captured = capsys.readouterr()
    assert "Test SA" in captured.out
