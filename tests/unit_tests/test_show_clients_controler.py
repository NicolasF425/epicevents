from unittest.mock import patch, MagicMock
from controlers.show_clients_controler import ShowClientsControler


@patch("controlers.show_clients_controler.get_client_by_id", return_value="fake_client")
@patch("controlers.show_clients_controler.ShowClientsControler.check_token_validity", return_value={"id": 42})
@patch("controlers.show_clients_controler.ShowSingleClientView")
def test_select_action_2(mock_view_cls, mock_token, mock_get_client):
    mock_view = MagicMock()
    mock_view_cls.return_value = mock_view

    controller = ShowClientsControler()
    controller.select_action("2", 123)

    mock_get_client.assert_called_with(123)
    mock_view.display_single_client.assert_called_with("fake_client")
