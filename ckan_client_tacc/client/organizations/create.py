import argparse
import json
from typing import Dict, List

import requests


def create_organization(org_data: Dict, api_key: str, ckan_url: str) -> bool:
    """Create a single organization in CKAN."""
    url = f"{ckan_url}/api/3/action/organization_create"
    headers = {"Authorization": api_key, "Content-Type": "application/json"}

    try:
        response = requests.post(url, json=org_data, headers=headers)
        response.raise_for_status()
        print(f"Successfully created organization: {org_data.get('name', 'unknown')}")
        return True
    except requests.exceptions.RequestException as e:
        print(
            f"Error creating organization {org_data.get('name', 'unknown')}: {str(e)}"
        )
        return False
