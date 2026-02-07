import requests

from requests.auth import HTTPBasicAuth

from config import BaseConfig
from models.employees import Employee


id = BaseConfig.get_config("id")
pwd = BaseConfig.get_config("")
api_root = "https://api.hibob.com"
service_path = "v1/people/search"

payload = {"showInactive": False}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
}


# import base64
# basic_auth_token = base64.b64encode(bytes("user:pass", "utf-8"))
basic_auth = HTTPBasicAuth(id, pwd)

search_url = api_root + "/" + service_path
search_response = requests.post(
    search_url,
    json=payload,
    headers=headers,
    auth=basic_auth,
)

search_results = search_response.json()

for result in search_results.get("employees", []):
    employee = Employee(result)
