#!/usr/bin/python3

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = int(sys.argv[1])

user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

user_response = requests.get(user_url)
todos_response = requests.get(todos_url)

if user_response.status_code != 200 or todos_response.status_code != 200:
    print("Failed to retrieve data")
    sys.exit(1)

user_data = user_response.json()
todos_data = todos_response.json()


employee_name = user_data.get("name")
total_tasks = len(todos_data)
done_tasks = [task for task in todos_data if task.get("completed")]


number_of_done_tasks = len(done_tasks)

print(f"Employee {employee_name} id done with tasks ({number_of_done_tasks}):")
for task in done_tasks:
    print(f"/t {task.get('title')}")
