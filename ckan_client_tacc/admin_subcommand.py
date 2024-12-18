import json
import os

import typer

from ckan_client_tacc.client.organizations.members.add import (
    Member,
    add_user_to_org_api,
    get_members,
)
from ckan_client_tacc.client.users.get import get_user_by_id, get_user_by_username
from ckan_client_tacc.models.tacc.user import ORG_ALLOCATION_MAPPING, Response, TaccUser

app = typer.Typer()

API_KEY = os.getenv("CKAN_API_KEY")
CKAN_URL = os.getenv("CKAN_URL")

if not API_KEY or not CKAN_URL:
    print("CKAN_API_KEY and CKAN_URL must be set")
    exit(1)


def create_user(user: TaccUser):
    pass


def get_or_create_user(user: TaccUser):
    try:
        get_user_by_username(CKAN_URL, API_KEY, user.username)
    except Exception as e:
        print(f"User {user.username} does not exist, creating...")
        create_user(user)


def add_user_to_org(user: TaccUser, org_id: str):
    print(f"Adding user {user.username} to organization {org_id}")


def convert_member_to_user(member: Member) -> TaccUser:
    user = get_user_by_id(CKAN_URL, API_KEY, member.id)
    return TaccUser(user)


def sync_tacc_allocations_org(allocation_id: str, org_id: str, folder: str):
    data = read_allocation_file(allocation_id, folder)
    members = get_members(CKAN_URL, API_KEY, org_id)
    users_members = [convert_member_to_user(member) for member in members]
    response = Response(data)
    for user in response.users:
        get_or_create_user(user)
        if user not in users_members:
            add_user_to_org(user, org_id)


def read_allocation_file(allocation_id: str, folder: str) -> dict:
    with open(f"{folder}/{allocation_id}.json", "r") as f:
        return json.load(f)


@app.command()
def sync_users(folder: str):
    """Sync users from TACC to CKAN"""
    for org_name, allocation_id in ORG_ALLOCATION_MAPPING.items():
        sync_tacc_allocations_org(allocation_id, org_name, folder)
        print(f"Synced {org_name} allocations from folder {folder}")
