import json
import os
from typing import List

import typer
from colorama import Fore, Style, init

from ckan_client_tacc.client.organizations.members.add import (
    add_user_to_org,
    convert_member_to_user,
    get_members,
)
from ckan_client_tacc.client.users.create import create_user_api
from ckan_client_tacc.client.users.get import get_user_by_id, get_user_by_username
from ckan_client_tacc.models.ckan.user import CkanUser
from ckan_client_tacc.models.portalx.user import OrganizationEnum, PortalXUser, Response
from ckan_client_tacc.models.UserMapper import ORG_ALLOCATION_MAPPING, UserMapper

app = typer.Typer()

API_KEY = os.getenv("CKAN_API_KEY")
CKAN_URL = os.getenv("CKAN_URL")

if not API_KEY or not CKAN_URL:
    print("CKAN_API_KEY and CKAN_URL must be set")
    exit(1)

init()  # Initialize colorama


def create_user(user: PortalXUser):
    create_user_api(CKAN_URL, API_KEY, UserMapper.map_to_ckan_user_request(user))


def get_or_create_user(user: PortalXUser) -> CkanUser:
    try:
        ckan_user = get_user_by_username(CKAN_URL, API_KEY, user.username)
        print(
            f"{Fore.YELLOW}👤 User {Fore.GREEN}{user.username}{Fore.YELLOW} already exists{Style.RESET_ALL}"
        )
        return ckan_user
    except Exception as e:
        ckan_user_request = UserMapper.map_to_ckan_user_request(user)
        try:
            print(
                f"{Fore.GREEN}✨ Creating user {ckan_user_request.name}{Style.RESET_ALL}"
            )
            create_user_api(CKAN_URL, API_KEY, ckan_user_request)
            ckan_user = get_user_by_username(CKAN_URL, API_KEY, user.username)
            print(f"{Fore.GREEN}✨ Created user {ckan_user.name}{Style.RESET_ALL}")
            return ckan_user
        except Exception as e:
            print(
                f"{Fore.RED}❌ Error creating user {user.username}: {e}{Style.RESET_ALL}"
            )


def create_users_on_ckan(portalx_users: List[PortalXUser]) -> List[CkanUser]:
    ckan_users = []
    for portalx_user in portalx_users:
        ckan_user = get_or_create_user(portalx_user)
        ckan_users.append(ckan_user)
    return ckan_users


def add_users_to_org(ckan_users: List[CkanUser], org_id: str):
    for ckan_user in ckan_users:
        print(f"Adding user {ckan_user.name} to organization {org_id}")
        add_user_to_org(CKAN_URL, API_KEY, ckan_user, org_id)
    print(
        f"{Fore.CYAN}➕ Added {len(ckan_users)} users to organization {org_id}{Style.RESET_ALL}"
    )


def sync_tacc_allocations_org(org_id: OrganizationEnum, json_file: str):
    org_name = ORG_ALLOCATION_MAPPING[org_id]
    print(
        f"{Fore.BLUE}🔄 Syncing {Fore.YELLOW}{org_name}{Fore.BLUE} allocations from folder {json_file}{Style.RESET_ALL}"
    )
    tacc_users = read_tacc_allocation_users(json_file)
    ckan_users = create_users_on_ckan(tacc_users)
    add_users_to_org(ckan_users, org_id)


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
