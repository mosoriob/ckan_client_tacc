from typing import Dict, List, Optional

import requests


def list_users(ckan_url: str, api_key: str, q: Optional[str] = None) -> List[Dict]:
    """List all users from CKAN.

    Args:
        api_key (str): CKAN API key
        ckan_url (str): CKAN instance URL
        q (str, optional): Search query to filter users

    Returns:
        List[Dict]: List of user dictionaries containing user information
    """
    url = f"{ckan_url}/api/3/action/user_list"
    headers = {"Authorization": api_key, "Content-Type": "application/json"}
    params = {}

    if q:
        params["q"] = q

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        users = response.json()["result"]
        print(f"Successfully retrieved {len(users)} users")
        return users
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving users: {str(e)}")
        return []
