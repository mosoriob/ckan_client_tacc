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


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Create organizations in CKAN from a JSON file."
    )
    parser.add_argument("--api-key", required=True, help="Your CKAN API key")
    parser.add_argument(
        "--json-file",
        required=True,
        help="Path to JSON file containing organization data",
    )
    parser.add_argument(
        "--ckan-url", default="https://ckan.tacc.utexas.edu", help="CKAN instance URL"
    )
    args = parser.parse_args()

    # Configuration
    CKAN_URL = args.ckan_url
    API_KEY = args.api_key
    JSON_FILE = args.json_file

    # Read organizations from JSON file
    try:
        with open(JSON_FILE, "r") as f:
            organizations = json.load(f)
    except FileNotFoundError:
        print(f"Error: {JSON_FILE} not found")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {JSON_FILE}")
        return

    # Create each organization
    success_count = 0
    for org in organizations:
        if create_organization(org, API_KEY, CKAN_URL):
            success_count += 1

    print(f"\nCreated {success_count} out of {len(organizations)} organizations")


if __name__ == "__main__":
    main()
