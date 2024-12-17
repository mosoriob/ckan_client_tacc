from typing import Dict, Optional

import requests


def get_user_by_id(ckan_url: str, api_key: str, user_id: str) -> Optional[Dict]:
    """
    Retrieve user information by user ID from CKAN.

    Args:
        user_id (str): The ID of the user to retrieve

    Returns:
        Optional[Dict]: User data if found, None if not found
    """
    url = f"{ckan_url}/api/3/action/user_show"
    headers = {"Authorization": api_key, "Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, params={"id": user_id})
        response.raise_for_status()

        data = response.json()
        return data["result"] if data["success"] else None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching user: {e}")
        return None
