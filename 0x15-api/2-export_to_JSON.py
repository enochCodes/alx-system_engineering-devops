import json
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 script.py <employee_id>")
    sys.exit(1)

employee_id = int(sys.argv[1])

# URLs to fetch the user and todo data
user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

# Fetch user data
user_response = requests.get(user_url)
if user_response.status_code != 200:
    print("Failed to retrieve user data")
    sys.exit(1)

user_data = user_response.json()

# Fetch todos data
todos_response = requests.get(todos_url)
if todos_response.status_code != 200:
    print("Failed to retrieve todos data")
    sys.exit(1)

todos_data = todos_response.json()

# Extract necessary information
employee_name = user_data.get("username")

# Prepare data for JSON export
tasks = []
for task in todos_data:
    task_info = {
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": employee_name
    }
    tasks.append(task_info)

json_data = {str(employee_id): tasks}

# Define the JSON filename
json_filename = f"{employee_id}.json"

# Write data to JSON file
with open(json_filename, mode='w') as file:
    json.dump(json_data, file)

print(f"Data exported to {json_filename}")
