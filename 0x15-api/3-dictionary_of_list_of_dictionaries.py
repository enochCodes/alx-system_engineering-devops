#!/usr/bin/python3

"""
dump all
"""

import json
import requests

# URLs to fetch the users and todos data
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

# Fetch users data
users_response = requests.get(users_url)
if users_response.status_code != 200:
    print("Failed to retrieve users data")
    sys.exit(1)

users_data = users_response.json()

# Fetch todos data
todos_response = requests.get(todos_url)
if todos_response.status_code != 200:
    print("Failed to retrieve todos data")
    sys.exit(1)

todos_data = todos_response.json()

# Prepare data for JSON export
todos_by_user = {}
for user in users_data:
    user_id = user["id"]
    username = user["username"]
    todos_by_user[user_id] = []
    for task in todos_data:
        if task["userId"] == user_id:
            task_info = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            todos_by_user[user_id].append(task_info)

# Define the JSON filename
json_filename = "todo_all_employees.json"

# Write data to JSON file
with open(json_filename, mode='w') as file:
    json.dump(todos_by_user, file, indent=4)

print(f"Data exported to {json_filename}")
