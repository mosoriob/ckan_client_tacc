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
