from dataclasses import dataclass

import requests

from ckan_client_tacc.models.tacc.user import TaccUser


@dataclass
class Member:
    """Class representing an organization member."""

    id: str
    type: str  # typically 'user'
    role: str  # 'Admin' or 'Member'


def add_user_to_org_api(ckan_url: str, api_key: str, user: TaccUser, org_id: str):
    url = f"{ckan_url}/api/3/action/organization_member_create"
    headers = {"Authorization": api_key, "Content-Type": "application/json"}
    data = {"id": org_id, "username": user.username}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()


def remove_user_from_org_api(ckan_url: str, api_key: str, user: TaccUser, org_id: str):
    url = f"{ckan_url}/api/3/action/organization_member_delete"
    headers = {"Authorization": api_key, "Content-Type": "application/json"}
    data = {"id": org_id, "username": user.username}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()


def get_members(ckan_url: str, api_key: str, org_id: str) -> list[Member]:
    url = f"{ckan_url}/api/3/action/member_list"
    headers = {"Authorization": api_key, "Content-Type": "application/json"}
    data = {"id": org_id}
    response = requests.get(url, headers=headers, params={"id": org_id})
    response.raise_for_status()
    return [Member(id=m[0], type=m[1], role=m[2]) for m in response.json()["result"]]
