from typing import Any

def get_active_users(users: list[dict[str, Any]]) -> list[str]:
    """Returns a list of names of users who are currently active."""
    return [user["name"] for user in users if user["active"]]

users = [
    {"name": "Aarav", "active": True},
    {"name": "Meera", "active": False},
    {"name": "Riya", "active": True},
]

if __name__ == "__main__":
    print(get_active_users(users))