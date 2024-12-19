import argparse
import json
from dataclasses import asdict, dataclass
from typing import Dict, Optional

import requests


@dataclass
class CkanUserRequest:
    """
    Dataclass representing a CKAN user creation request

    Args:
        name: Username (2-100 chars, lowercase alphanumeric, - and _)
        email: User email address
        password: User password (min 4 chars)
        fullname: Optional full name of the user
        about: Optional description of the user
        image_url: Optional URL to user's profile image
        id: Optional specific user ID
        plugin_extras: Optional plugin-specific data (sysadmin only)
    """

    name: str
    email: str
    password: str
    fullname: Optional[str] = None
    about: Optional[str] = None
    image_url: Optional[str] = None
    id: Optional[str] = None
    plugin_extras: Optional[Dict] = None

    def to_dict(self) -> Dict:
        """Convert to dict, excluding None values"""
        return {k: v for k, v in asdict(self).items() if v is not None}


def create_user_api(api_url: str, api_key: str, user_data: CkanUserRequest) -> Dict:
    """
    Create a new CKAN user using the API

    Args:
        api_url: The base URL of the CKAN instance
        api_key: Admin API key with permission to create users
        user_data: CkanUserRequest object containing user details

    Returns:
        Dict: Response from the CKAN API
    """
    headers = {"Authorization": api_key, "Content-Type": "application/json"}
    endpoint = f"{api_url.rstrip('/')}/api/3/action/user_create"

    try:
        response = requests.post(
            endpoint, headers=headers, data=json.dumps(user_data.to_dict())
        )
        print(response.json())
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating user: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(description="Create a new CKAN user")
    parser.add_argument("--api-url", required=True, help="CKAN API URL")
    parser.add_argument("--api-key", required=True, help="Admin API key")
    parser.add_argument(
        "--name",
        required=True,
        help="Username (2-100 chars, lowercase alphanumeric, - and _)",
    )
    parser.add_argument("--email", required=True, help="User email")
    parser.add_argument("--password", required=True, help="User password (min 4 chars)")
    parser.add_argument("--fullname", help="Full name of the user")
    parser.add_argument("--about", help="Description of the user")
    parser.add_argument("--image-url", help="URL to user's profile image")
    parser.add_argument("--id", help="Specific user ID (optional)")

    args = parser.parse_args()

    user_request = CkanUserRequest(
        name=args.name,
        email=args.email,
        password=args.password,
        fullname=args.fullname,
        about=args.about,
        image_url=args.image_url,
        id=args.id,
    )

    try:
        result = create_user_api(args.api_url, args.api_key, user_request)
        if result.get("success"):
            print(f"User '{args.name}' created successfully!")
            print(f"User ID: {result['result']['id']}")
        else:
            print(f"Failed to create user: {result.get('error', 'Unknown error')}")
    except Exception as e:
        print(f"Error creating user: {e}")


if __name__ == "__main__":
    main()
