import argparse
import json
from typing import Dict, Optional

import requests


def get_dataset(dataset_name: str, api_key: str, ckan_url: str) -> Optional[Dict]:
    """Get details of a specific dataset from CKAN."""
    url = f"{ckan_url}/api/3/action/package_show"
    headers = {"Authorization": api_key, "Content-Type": "application/json"}
    params = {"id": dataset_name}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        dataset = response.json()["result"]
        return dataset
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving dataset {dataset_name}: {str(e)}")
        return None


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Get details of a specific CKAN dataset."
    )
    parser.add_argument("--api-key", required=True, help="Your CKAN API key")
    parser.add_argument(
        "--dataset-name", required=True, help="Name of the dataset to retrieve"
    )
    parser.add_argument(
        "--ckan-url", default="https://ckan.tacc.utexas.edu", help="CKAN instance URL"
    )
    parser.add_argument(
        "--output-file", help="Optional JSON file to save the dataset details"
    )
    args = parser.parse_args()

    # Get dataset details
    dataset = get_dataset(args.dataset_name, args.api_key, args.ckan_url)

    if dataset:
        if args.output_file:
            try:
                with open(args.output_file, "w") as f:
                    json.dump(dataset, f, indent=2)
                print(f"Dataset details saved to {args.output_file}")
            except IOError as e:
                print(f"Error saving to file: {str(e)}")
        else:
            # Print dataset details to console
            print(json.dumps(dataset, indent=2))
    else:
        print(f"Dataset '{args.dataset_name}' not found or error occurred")


if __name__ == "__main__":
    main()
