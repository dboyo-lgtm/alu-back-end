#!/usr/bin/python3
"""
A Python script that returns an employee's TODO list progress
using a REST API.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_res = requests.get(f"{base_url}/users/{employee_id}")
    todos_res = requests.get(f"{base_url}/todos", params={"userId": employee_id})

    user_data = user_res.json()
    todos_data = todos_res.json()

    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    completed_tasks = [t for t in todos_data if t.get("completed")]
    number_of_done_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t {task.get('title')}")
