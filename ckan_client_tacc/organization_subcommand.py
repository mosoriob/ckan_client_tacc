import json
import os

import typer

from ckan_client_tacc.client.organizations.create import create_organization

app = typer.Typer()

API_KEY = os.getenv("CKAN_API_KEY")
CKAN_URL = os.getenv("CKAN_URL")

if not API_KEY or not CKAN_URL:
    print("CKAN_API_KEY and CKAN_URL must be set")
    exit(1)


@app.command(
    name="create",
    help="Create an organization or organizations in TACC data discovery from a JSON file",
)
def create(json_file: str):
    with open(json_file, "r") as f:
        organizations = json.load(f)

    if not isinstance(organizations, list):
        organizations = [organizations]

    success_count = 0
    for organization in organizations:
        create_organization(organization, API_KEY, CKAN_URL)
        success_count += 1

    print(f"\nCreated {success_count} out of {len(organizations)} organizations")
