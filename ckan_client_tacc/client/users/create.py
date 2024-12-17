import argparse
import json
from typing import Dict

import requests


def create_user(api_url: str, api_key: str, user_data: Dict) -> Dict:
    """
    Create a new CKAN user using the API

    Args:
        api_url: The base URL of the CKAN instance
        api_key: Admin API key with permission to create users
        user_data: Dictionary containing user details

    Returns:
        Dict: Response from the CKAN API
    """
    headers = {"Authorization": api_key, "Content-Type": "application/json"}

    endpoint = f"{api_url.rstrip('/')}/api/3/action/user_create"

    try:
        response = requests.post(endpoint, headers=headers, data=json.dumps(user_data))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating user: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(description="Create a new CKAN user")
    parser.add_argument("--api-url", required=True, help="CKAN API URL")
    parser.add_argument("--api-key", required=True, help="Admin API key")
    parser.add_argument("--name", required=True, help="Username")
    parser.add_argument("--email", required=True, help="User email")
    parser.add_argument("--password", required=True, help="User password")
    parser.add_argument("--fullname", help="Full name of the user")

    args = parser.parse_args()

    user_data = {
        "name": args.name,
        "email": args.email,
        "password": args.password,
    }

    if args.fullname:
        user_data["fullname"] = args.fullname

    try:
        result = create_user(args.api_url, args.api_key, user_data)
        if result.get("success"):
            print(f"User '{args.name}' created successfully!")
            print(f"User ID: {result['result']['id']}")
        else:
            print(f"Failed to create user: {result.get('error', 'Unknown error')}")
    except Exception as e:
        print(f"Error creating user: {e}")


if __name__ == "__main__":
    main()
