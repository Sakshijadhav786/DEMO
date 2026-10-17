def calculate_average(numbers):
    """Calculates the average of a list of numbers. Returns 0 if the list is empty."""
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)


def get_user_name(users, user_id):
    """Searches for a user name by ID within a list of user dictionaries."""
    for user in users:
        if user["id"] == user_id:
            return user["name"]
    return None


# Test Case 1: Standard list
numbers = [10, 20, 30]
print("Average:", calculate_average(numbers))

# Test Case 2: Empty list (Fixed: Now returns 0 instead of crashing)
empty_numbers = []
print("Average (empty):", calculate_average(empty_numbers))

# Test Case 3: User lookup (Fixed: Passed user inside a list to match expected input type)
user = {"id": 1, "name": "Aarav"}
print("Username:", get_user_name([user], 1))