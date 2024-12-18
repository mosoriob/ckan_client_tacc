from dataclasses import dataclass
from typing import List, Literal, Tuple


@dataclass
class Member:
    id: str
    type: Literal["user"]
    role: Literal["Admin", "Member"]

    def __init__(self, data: Tuple[str, Literal["user"], Literal["Admin", "Member"]]):
        self.id = data[0]
        self.type = data[1]
        self.role = data[2]


@dataclass
class MemberResponse:
    help: str
    success: bool
    result: List[Member]

    @classmethod
    def from_response(cls, response: dict):
        return cls(**response)
