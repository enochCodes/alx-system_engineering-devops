#!/usr/bin/python3

"""export to csv
"""
import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 1-export_to_CSV.py <employee_id>")
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

# Define the CSV filename
csv_filename = f"{employee_id}.csv"

# Write data to CSV
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    for task in todos_data:
        writer.writerow([
            employee_id,
            employee_name,
            task.get("completed"),
            task.get("title")
            ])

print(f"Data exported to {csv_filename}")
