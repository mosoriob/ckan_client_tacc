from dataclasses import dataclass
from typing import List

ORG_ALLOCATION_MAPPING = {
    "planet-texas-2050": "BCS2411",
    "SETx-UIFL": "CA23001",
    "dynamo": "BCS24008",
}


@dataclass
class TaccUser:
    id: str
    username: str
    role: str
    first_name: str
    last_name: str
    email: str


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
