import argparse
import json
from typing import Dict, List

import requests


def list_datasets(api_key: str, ckan_url: str) -> List[Dict]:
    """List all datasets from CKAN."""
    url = f"{ckan_url}/api/3/action/package_list"
    headers = {"Authorization": api_key, "Content-Type": "application/json"}

    try:
        # Get list of dataset names
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        dataset_names = response.json()["result"]

        # Get detailed information for each dataset
        datasets = []
        for name in dataset_names:
            detail_url = f"{ckan_url}/api/3/action/package_show"
            detail_response = requests.get(
                detail_url, headers=headers, params={"id": name}
            )
            detail_response.raise_for_status()
            dataset_info = detail_response.json()["result"]
            datasets.append(dataset_info)

        print(f"Successfully retrieved {len(datasets)} datasets")
        return datasets
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving datasets: {str(e)}")
        return []


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="List datasets from CKAN instance.")
    parser.add_argument("--api-key", required=True, help="Your CKAN API key")
    parser.add_argument(
        "--ckan-url", default="https://ckan.tacc.utexas.edu", help="CKAN instance URL"
    )
    parser.add_argument(
        "--output-file", help="Optional JSON file to save the dataset list"
    )
    args = parser.parse_args()

    # Configuration
    CKAN_URL = args.ckan_url
    API_KEY = args.api_key

    # Get datasets
    datasets = list_datasets(API_KEY, CKAN_URL)

    # Output results
    if args.output_file:
        try:
            with open(args.output_file, "w") as f:
                json.dump(datasets, f, indent=2)
            print(f"Dataset list saved to {args.output_file}")
        except IOError as e:
            print(f"Error saving to file: {str(e)}")
    else:
        # Print dataset names to console
        for dataset in datasets:
            print(f"Dataset: {dataset.get('name')} - Title: {dataset.get('title')}")


if __name__ == "__main__":
    main()
