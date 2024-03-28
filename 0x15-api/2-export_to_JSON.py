#!/usr/bin/python3
"""Python script that, using a REST API"""
import csv
import json
from requests import get
from sys import argv


if __name__ == "__main__":

    response1 = get('https://jsonplaceholder.typicode.com/todos/')
    todo_data = response1.json()
    user_id = int(argv[1])

    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()
    name = [res for res in data2 if res["id"] == user_id]
    name = name[0]["username"]

    todo_data_filtered_before = [
        res for res in todo_data if res["userId"] == user_id]
    row = []

    for i in todo_data_filtered_before:

        new_dict = {}

        if i['userId'] == int(argv[1]):
            new_dict['task'] = i['title']
            new_dict['completed'] = i['completed']
            new_dict['username'] = name
            row.append(new_dict)

    final_dict = {}
    final_dict[user_id] = row
    print(final_dict)

    json_obj = json.dumps(final_dict)

    with open(argv[1] + ".json", "w") as f:
        f.write(json_obj)
