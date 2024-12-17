import argparse
import json
from typing import Dict, List, Optional

import requests


def create_resource(
    dataset_name: str, resource_data: Dict, api_key: str, ckan_url: str
) -> Optional[Dict]:
    """Create a new resource in a CKAN dataset."""
    url = f"{ckan_url}/api/3/action/resource_create"
    headers = {"Authorization": api_key, "Content-Type": "application/json"}

    # Ensure the resource is associated with the dataset
    resource_data["package_id"] = dataset_name

    try:
        response = requests.post(url, json=resource_data, headers=headers)
        response.raise_for_status()
        resource = response.json()["result"]
        print(f"Successfully created resource: {resource.get('name', 'unnamed')}")
        return resource
    except requests.exceptions.RequestException as e:
        print(f"Error creating resource: {str(e)}")
        return None


def validate_resource(resource_data: Dict) -> bool:
    """Validate required fields for resource creation."""
    required_fields = ["url"]
    for field in required_fields:
        if field not in resource_data:
            print(f"Error: Missing required field '{field}' in resource data")
            return False
    return True


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Create resources in a CKAN dataset.")
    parser.add_argument("--api-key", required=True, help="Your CKAN API key")
    parser.add_argument(
        "--dataset-name",
        required=True,
        help="Name of the dataset to add the resources to",
    )
    parser.add_argument(
        "--json-file", required=True, help="Path to JSON file containing resource data"
    )
    parser.add_argument(
        "--ckan-url", default="https://ckan.tacc.utexas.edu", help="CKAN instance URL"
    )
    args = parser.parse_args()

    # Read resources from JSON file
    try:
        with open(args.json_file, "r") as f:
            resources = json.load(f)
    except FileNotFoundError:
        print(f"Error: {args.json_file} not found")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {args.json_file}")
        return

    # Ensure resources is a list
    if not isinstance(resources, list):
        resources = [resources]

    # Create each resource
    success_count = 0
    for resource_data in resources:
        # Remove any None values
        resource_data = {k: v for k, v in resource_data.items() if v is not None}

        if validate_resource(resource_data):
            resource = create_resource(
                args.dataset_name, resource_data, args.api_key, args.ckan_url
            )
            if resource:
                success_count += 1

    print(f"\nCreated {success_count} out of {len(resources)} resources")


if __name__ == "__main__":
    main()
