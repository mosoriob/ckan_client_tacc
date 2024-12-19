import json
import os
from typing import List

import typer

from ckan_client_tacc.client.organizations.members.add import (
    convert_member_to_user,
    get_members,
)
from ckan_client_tacc.client.users.create import create_user_api
from ckan_client_tacc.client.users.get import get_user_by_id, get_user_by_username
from ckan_client_tacc.models.portalx.user import OrganizationEnum, PortalXUser, Response
from ckan_client_tacc.models.UserMapper import UserMapper

app = typer.Typer()

API_KEY = os.getenv("CKAN_API_KEY")
CKAN_URL = os.getenv("CKAN_URL")

if not API_KEY or not CKAN_URL:
    print("CKAN_API_KEY and CKAN_URL must be set")
    exit(1)


def create_user(user: PortalXUser):
    create_user_api(CKAN_URL, API_KEY, UserMapper.map_to_ckan_user_request(user))


def get_or_create_user(user: PortalXUser):
    try:
        get_user_by_username(CKAN_URL, API_KEY, user.name)
    except Exception as e:
        print(f"User does not exist, creating...")
        create_user_api(CKAN_URL, API_KEY, UserMapper.map_to_ckan_user_request(user))


def add_user_to_org(user: PortalXUser, org_id: str):
    print(f"Adding user {user.name} to organization {org_id}")


def sync_tacc_allocations_org(org_id: OrganizationEnum, json_file: str):
    print(f"Syncing {org_id} allocations from folder {json_file}")
    tacc_users = read_tacc_allocation_users(json_file)
    print(f"Found {len(tacc_users)} users")
    org_members = get_members(CKAN_URL, API_KEY, org_id.value)
    print(f"Found {len(org_members)} members")
    org_members_users = [
        convert_member_to_user(CKAN_URL, API_KEY, member) for member in org_members
    ]
    print(f"Found {len(org_members_users)} members")
    for user in tacc_users:
        print(user)
        # get_or_create_user(user)
        # if user not in org_members_users:
        #    add_user_to_org(user, org_id)


def read_tacc_allocation_users(json_file: str) -> List[PortalXUser]:
    with open(json_file, "r") as f:
        return [PortalXUser(**user) for user in json.load(f)["response"]]


def read_allocation_file(json_file: str) -> dict:
    with open(json_file, "r") as f:
        return json.load(f)


@app.command(
    name="sync",
    help="Sync users from TACC allocations to CKAN organizations",
)
def sync(organization: OrganizationEnum, json_file: str):
    sync_tacc_allocations_org(organization, json_file)
    # print(f"Synced {organization} allocations from folder {json_file}")
