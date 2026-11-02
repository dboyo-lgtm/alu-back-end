#!/usr/bin/python3
"""
A Python script to export an employee's TODO list data in JSON format.
"""

json = __import__('json')
requests = __import__('requests')
sys = __import__('sys')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_res = requests.get(f"{base_url}/users/{employee_id}")
    todos_res = requests.get(f"{base_url}/todos", params={"userId": employee_id})

    user_data = user_res.json()
    todos_data = todos_res.json()

    username = user_data.get("username")

    task_list = []
    for task in todos_data:
        task_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    out_data = {employee_id: task_list}

    filename = f"{employee_id}.json"
    with open(filename, mode="w") as json_file:
        json.dump(out_data, json_file)
