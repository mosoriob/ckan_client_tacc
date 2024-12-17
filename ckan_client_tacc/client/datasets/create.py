import argparse
import json
from typing import Dict

import requests


def create_dataset(dataset_data: Dict, api_key: str, ckan_url: str) -> bool:
    """Create a single dataset in CKAN."""
    url = f"{ckan_url}/api/3/action/package_create"
    headers = {"Authorization": api_key, "Content-Type": "application/json"}

    try:
        response = requests.post(url, json=dataset_data, headers=headers)
        response.raise_for_status()
        print(f"Successfully created dataset: {dataset_data.get('name', 'unknown')}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error creating dataset {dataset_data.get('name', 'unknown')}: {str(e)}")
        return False


def validate_dataset(dataset: Dict) -> bool:
    """Validate required fields for dataset creation."""
    required_fields = ["name", "title"]
    for field in required_fields:
        if field not in dataset:
            print(f"Error: Missing required field '{field}' in dataset")
            return False
    return True


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Create datasets in CKAN from a JSON file."
    )
    parser.add_argument("--api-key", required=True, help="Your CKAN API key")
    parser.add_argument(
        "--json-file", required=True, help="Path to JSON file containing dataset data"
    )
    parser.add_argument(
        "--ckan-url", default="https://ckan.tacc.utexas.edu", help="CKAN instance URL"
    )
    args = parser.parse_args()

    # Configuration
    CKAN_URL = args.ckan_url
    API_KEY = args.api_key
    JSON_FILE = args.json_file

    # Read datasets from JSON file
    try:
        with open(JSON_FILE, "r") as f:
            datasets = json.load(f)
    except FileNotFoundError:
        print(f"Error: {JSON_FILE} not found")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {JSON_FILE}")
        return

    # Ensure datasets is a list
    if not isinstance(datasets, list):
        datasets = [datasets]

    # Create each dataset
    success_count = 0
    for dataset in datasets:
        if validate_dataset(dataset) and create_dataset(dataset, API_KEY, CKAN_URL):
            success_count += 1

    print(f"\nCreated {success_count} out of {len(datasets)} datasets")


if __name__ == "__main__":
    main()
