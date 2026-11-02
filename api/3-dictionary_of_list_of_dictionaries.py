#!/usr/bin/python3
"""
A Python script to export all employees' TODO lists data in JSON format.
"""

json = __import__('json')
requests = __import__('requests')


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_res = requests.get(f"{base_url}/users")
    todos_res = requests.get(f"{base_url}/todos")

    users = users_res.json()
    todos = todos_res.json()

    user_dict = {user.get("id"): user.get("username") for user in users}

    all_data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user_id
        ]
        all_data[str(user_id)] = user_tasks

    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump(all_data, json_file)
