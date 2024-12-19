from dataclasses import dataclass
from typing import List

ORG_ALLOCATION_MAPPING = {
    "planet-texas-2050": "BCS2411",
    "setx-uifl": "CA23001",
    "dynamo": "BCS24008",
}


@dataclass
class TaccUser:
    id: str
    name: str
    fullname: str
    created: str
    about: str
    activity_streams_email_notifications: bool
    sysadmin: bool
    state: str
    image_url: str
    display_name: str
    email_hash: str
    number_created_packages: int
    apikey: str
    email: str
    image_display_url: str

    def __init__(self, data: dict):
        self.id = data["id"]
        self.name = data["name"]
        self.fullname = data["fullname"]
        self.created = data["created"]
        self.about = data["about"]
        self.activity_streams_email_notifications = data[
            "activity_streams_email_notifications"
        ]
        self.sysadmin = data["sysadmin"]
        self.state = data["state"]
        self.image_url = data["image_url"]
        self.display_name = data["display_name"]
        self.email_hash = data["email_hash"]
        self.number_created_packages = data["number_created_packages"]
        self.apikey = data["apikey"]
        self.email = data["email"]
        self.image_display_url = data["image_display_url"]


@dataclass
class Response:
    users: List[TaccUser]

    @classmethod
    def from_response(cls, response):
        users = [
            TaccUser(
                id=item["id"],
                username=item["username"],
                role=item["role"],
                first_name=item["firstName"],
                last_name=item["lastName"],
                email=item["email"],
            )
            for item in response["response"]
        ]
        return cls(users=users)
