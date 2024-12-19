import json
import os

import typer

from ckan_client_tacc.client.datasets.create import create_dataset, validate_dataset

app = typer.Typer()

API_KEY = os.getenv("CKAN_API_KEY")
CKAN_URL = os.getenv("CKAN_URL")

if not API_KEY or not CKAN_URL:
    print("CKAN_API_KEY and CKAN_URL must be set")
    exit(1)


@app.command(
    name="create",
    help="Create a dataset(s) from a JSON file",
)
def create(json_file: str):
    with open(json_file, "r") as f:
        datasets = json.load(f)

    if not isinstance(datasets, list):
        datasets = [datasets]

    success_count = 0
    for dataset in datasets:
        if validate_dataset(dataset) and create_dataset(dataset, API_KEY, CKAN_URL):
            success_count += 1
        else:
            print(f"Failed to create dataset: {dataset['name']}")
    print(f"\nCreated {success_count} out of {len(datasets)} datasets")
