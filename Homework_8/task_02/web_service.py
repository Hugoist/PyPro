import requests
from typing import Any, Dict


class WebService:
    """
    A class to fetch data from a given web service
    """

    def get_data(self, url: str) -> Dict[str, Any]:
        """
        Send a GET request to the given URL and return the JSON response
        """
        response = requests.get(url)
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()
