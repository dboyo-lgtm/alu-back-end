# API Project

This project contains Python scripts designed to interact with a REST API (`https://jsonplaceholder.typicode.com`), fetch user and TODO task data, display task completion progress, and export the information into CSV and JSON formats.

## Environment & Requirements
- **OS:** Ubuntu 14.04 LTS
- **Language:** Python 3 (version 3.4.3)
- **Style Guide:** PEP 8
- **Modules used:** `requests`, `csv`, `json`, `sys`

---

## Files and Tasks

| Filename | Description |
| :--- | :--- |
| `0-gather_data_from_an_API.py` | Accepts an employee ID as a parameter and prints their completed TODO tasks and progress. |
| `1-export_to_CSV.py` | Extends task 0 to export all tasks owned by a specific employee into a CSV file (`<USER_ID>.csv`). |
| `2-export_to_JSON.py` | Extends task 0 to export all tasks owned by a specific employee into a JSON file (`<USER_ID>.json`). |
| `3-dictionary_of_list_of_dictionaries.py` | Exports all TODO tasks for all employees into a single JSON file (`todo_all_employees.json`). |

---

## Usage

Make sure your files are executable:
```bash
chmod +x *.py
