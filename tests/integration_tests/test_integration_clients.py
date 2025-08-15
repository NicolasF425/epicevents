from unittest.mock import patch
from views.show_clients_view import ShowClientsView
from controlers.show_clients_controler import ShowClientsControler


@patch("views.show_clients_view.get_all_clients")
@patch("views.show_clients_view.clear_screen")
@patch("views.show_clients_view.ShowClientsView.check_token_validity", return_value={"id": 42})
@patch("views.show_clients_view.input", side_effect=["1", "123"])
def test_integration_display_clients(mock_input, mock_token, mock_clear, mock_get_all):
    fake_clients = [type("FakeClient", (), {"id": 123, "nom_entreprise": "Entreprise Test"})()]
    mock_get_all.return_value = fake_clients

    view = ShowClientsView()
    view.controler = ShowClientsControler()

    with patch.object(ShowClientsControler, "select_action") as mock_select:
        view.display_clients(filtered=False)
        # On attend maintenant un int en premier paramètre
        mock_select.assert_called_once_with("2", "123")
