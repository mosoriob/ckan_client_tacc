from dataclasses import dataclass
from typing import List


@dataclass
class CkanUser:
    id: str
    name: str
    fullname: str
    created: str
    about: str | None
    activity_streams_email_notifications: bool
    sysadmin: bool
    state: str
    image_url: str | None
    display_name: str
    email_hash: str
    email: str | None
    number_created_packages: int
    image_display_url: str | None
    apikey: str | None

    @classmethod
    def from_dict(cls, data: dict) -> "CkanUser":
        print(data)
        return cls(**data)


@dataclass
class Response:
    users: List[CkanUser]

    def __init__(self, response: dict):
        self.users = [CkanUser(**user) for user in response["result"]["users"]]
