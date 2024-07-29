#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"

    try:
        user_response = requests.get(url + "users/{}".format(employee_id))
        todos_response = requests.get(url + "todos",
                                      params={"userId": employee_id}
                                      )
        user_response.raise_for_status()
        todos_response.raise_for_status()
        user = user_response.json()
        todos = todos_response.json()
    except requests.RequestException:
        print("Error: Unable to fetch data from the API")
        sys.exit(1)

    if not user or "name" not in user:
        print("Error: Employee ID not found")
        sys.exit(1)

    employee_name = user.get("name")
    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    number_of_done_tasks = len(completed_tasks)

    # Display the results
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
