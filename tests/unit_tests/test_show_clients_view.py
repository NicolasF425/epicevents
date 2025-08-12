from unittest.mock import patch, MagicMock
from views.show_clients_view import ShowClientsView


@patch("views.show_clients_view.get_clients_by_idCommercial")
@patch("views.show_clients_view.ShowClientsView.check_token_validity", return_value={"id": 42})
@patch("views.show_clients_view.clear_screen")
def test_affichage_mes_clients(capsys, mock_clear, mock_token, mock_get_clients):
    # Faux client simulé
    fake_clients = [MagicMock(id=1, nom_entreprise="Entreprise E")]
    mock_get_clients.return_value = fake_clients

    view = ShowClientsView()
    view.controler = MagicMock()  # on remplace le contrôleur réel

    # Appel de la méthode à tester
    view.display_clients(filtered=True)

    # Capture de la sortie console
    out = capsys.readouterr().out
    assert "MES CLIENTS" in out
    assert "Entreprise E" in out
