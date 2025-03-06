import requests
import os

BASE_URL = "https://api.snyk.io/rest"
SNYK_TOKEN = os.getenv("SNYK_TOKEN")
API_VERSION = "version=2024-10-15"


def get_organizations():
    url = f"{BASE_URL}/orgs?{API_VERSION}"

    headers = {
        "Authorization": f"token {SNYK_TOKEN}",
        "Content-Type": "application/vnd.api+json",
        "Accept": "application/vnd.api+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        data = response.json().get("data", [])

        org_ids = [{"id": org["id"], "name": org["attributes"]["name"]} for org in data]
        return org_ids
    else:
        return None

orgs = get_organizations()
print("Returned Organizations:", orgs) 

