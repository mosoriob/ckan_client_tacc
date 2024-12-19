import json
import os
from typing import List

import typer
from colorama import Fore, Style, init

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

init()  # Initialize colorama


def create_user(user: PortalXUser):
    create_user_api(CKAN_URL, API_KEY, UserMapper.map_to_ckan_user_request(user))


def get_or_create_user(user: PortalXUser):
    try:
        get_user_by_username(CKAN_URL, API_KEY, user.username)
        print(f"{Fore.YELLOW}👤 User {user.username} already exists{Style.RESET_ALL}")
    except Exception as e:
        ckan_user = UserMapper.map_to_ckan_user_request(user)
        try:
            print(f"{Fore.GREEN}✨ Creating user {user.username}{Style.RESET_ALL}")
            create_user_api(CKAN_URL, API_KEY, ckan_user)
        except Exception as e:
            print(
                f"{Fore.RED}❌ Error creating user {user.username}: {e}{Style.RESET_ALL}"
            )


def add_user_to_org(user: PortalXUser, org_id: str):
    print(
        f"{Fore.CYAN}➕ Adding user {user.name} to organization {org_id}{Style.RESET_ALL}"
    )


def create_users_on_ckan(portalx_users: List[PortalXUser]):
    for portalx_user in portalx_users:
        get_or_create_user(portalx_user)


def sync_tacc_allocations_org(org_id: OrganizationEnum, json_file: str):
    print(
        f"{Fore.BLUE}🔄 Syncing {org_id} allocations from folder {json_file}{Style.RESET_ALL}"
    )
    tacc_users = read_tacc_allocation_users(json_file)
    create_users_on_ckan(tacc_users)


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
