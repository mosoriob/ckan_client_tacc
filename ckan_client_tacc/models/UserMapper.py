from dataclasses import asdict
from typing import Dict, List

from ckan_client_tacc.client.users.create import CkanUserRequest
from ckan_client_tacc.models.ckan.user import CkanUser
from ckan_client_tacc.models.tacc.user import TaccUser

ORG_ALLOCATION_MAPPING = {
    "planet-texas-2050": "BCS2411",
    "setx-uifl": "CA23001",
    "dynamo": "BCS24008",
}


class UserMapper:
    @staticmethod
    def map_to_ckan_user_request(tacc_user: TaccUser) -> CkanUserRequest:
        return CkanUserRequest(
            name=tacc_user.username,
            email=tacc_user.email,
            password=tacc_user.password,
            fullname=f"{tacc_user.first_name} {tacc_user.last_name}",
            about=None,
            image_url=None,
            id=None,
            plugin_extras=None,
        )

    @staticmethod
    def map_to_ckan_user(tacc_user: TaccUser) -> CkanUser:
        """Map a TaccUser to a CKAN User."""
        return CkanUser(
            id=tacc_user.id,
            name=tacc_user.username,
            fullname=f"{tacc_user.first_name} {tacc_user.last_name}",
            created="2024-01-01",  # Placeholder, adapt as needed
            about=None,
            activity_streams_email_notifications=False,  # Default value
            sysadmin=(tacc_user.role.lower() == "admin"),
            state="active" if tacc_user.role.lower() != "inactive" else "inactive",
            image_url=None,
            display_name=tacc_user.username,
            email_hash="",
            number_created_packages=0,
            image_display_url=None,
        )

    @staticmethod
    def map_from_ckan_user(ckan_user: CkanUser) -> TaccUser:
        """Map a CKAN User to a TaccUser."""
        first_name, _, last_name = (ckan_user.fullname or "").partition(" ")
        return TaccUser(
            id=ckan_user.id,
            username=ckan_user.name,
            role="admin" if ckan_user.sysadmin else "user",
            first_name=first_name,
            last_name=last_name,
            email=ckan_user.email_hash,  # Adjust if email is stored differently
        )

    @staticmethod
    def map_organization(tacc_org: str) -> str:
        """Map a TACC organization to a CKAN allocation."""
        if tacc_org in ORG_ALLOCATION_MAPPING:
            return ORG_ALLOCATION_MAPPING[tacc_org]
        else:
            raise ValueError(f"Organization {tacc_org} not found in mapping")
