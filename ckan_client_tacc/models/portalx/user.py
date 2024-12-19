from dataclasses import dataclass
from enum import Enum
from typing import List


class OrganizationEnum(str, Enum):
    PLANET_TEXAS_2050 = "planet-texas-2050"
    SETX_UIFL = "setx-uifl"
    DYNAMO = "dynamo"


class AllocationEnum(str, Enum):
    BCS2411 = "BCS2411"
    CA23001 = "CA23001"
    BCS24008 = "BCS24008"


ORG_ALLOCATION_MAPPING = {
    OrganizationEnum.PLANET_TEXAS_2050: AllocationEnum.BCS2411,
    OrganizationEnum.SETX_UIFL: AllocationEnum.CA23001,
    OrganizationEnum.DYNAMO: AllocationEnum.BCS24008,
}


@dataclass
class PortalXUser:
    id: str
    username: str
    role: str
    first_name: str
    last_name: str
    email: str

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def from_dict(cls, data: dict) -> "PortalXUser":
        print(data)
        return cls(**data)


@dataclass
class Response:
    users: List[PortalXUser]

    @classmethod
    def from_response(cls, response):
        users = [
            PortalXUser(
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
