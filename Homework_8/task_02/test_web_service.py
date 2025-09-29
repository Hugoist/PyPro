import unittest
from unittest.mock import patch, Mock
from web_service import WebService


class TestWebService(unittest.TestCase):
    """
    Unit tests for WebService with mocked requests
    """

    @patch("Homework_8.task_02.web_service.requests.get")
    def test_get_data_success(self, mock_get):
        """
        Test successful GET request returning JSON data.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "ololo"}
        mock_get.return_value = mock_response

        service = WebService()
        result = service.get_data("http://fakeurl.com")

        self.assertEqual(result, {"data": "ololo"})
        mock_get.assert_called_once_with("http://fakeurl.com")

    @patch("Homework_8.task_02.web_service.requests.get")
    def test_get_data_http_error(self, mock_get):
        """
        Test GET request that raises an HTTPError for non-200 status
        """
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = Exception("Not Found")
        mock_get.return_value = mock_response

        service = WebService()
        with self.assertRaises(Exception) as context:
            service.get_data("http://fakeurl.com")
        self.assertEqual(str(context.exception), "Not Found")
        mock_get.assert_called_once_with("http://fakeurl.com")


if __name__ == "__main__":
    unittest.main()
