import os
import requests

from datetime import date
from requests.auth import HTTPBasicAuth

from config import BaseConfig
from extractor import csv_dump
from models.employees import Employee, CompanyEmployees


class HibobApiClient:
    _api_root = "https://api.hibob.com"
    _service_path = "v1/people/search"
    _payload = {"showInactive": False}
    _headers = {
        "accept": "application/json",
        "content-type": "application/json",
    }

    def __init__(self) -> None:
        self._id: str = BaseConfig.get_config("id")
        self._pwd: str = BaseConfig.get_config("pwd")

    def call_search_api(self) -> requests.Response:
        basic_auth = HTTPBasicAuth(self._id, self._pwd)
        search_url = self._api_root + "/" + self._service_path

        return requests.post(
            search_url,
            json=self._payload,
            headers=self._headers,
            auth=basic_auth,
        )


def extract_employees_data() -> list[dict[str, str | None]]:
    hibob_api = HibobApiClient()
    search_response = hibob_api.call_search_api()

    if search_response.status_code == 200:
        search_results = search_response.json()
        return search_results.get("employees", [])
    else:
        raise Exception(
            f"API request failed with status code {search_response.status_code}"
        )
