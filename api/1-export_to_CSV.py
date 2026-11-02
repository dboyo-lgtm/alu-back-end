#!/usr/bin/python3
"""
A Python script to export an employee's TODO list data in CSV format.
"""

csv = __import__('csv')
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

    filename = f"{employee_id}.csv"
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])
