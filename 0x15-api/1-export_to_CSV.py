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
    todo_data_filtered_after = [
        res for res in todo_data
        if res["userId"] == user_id and res["completed"]]

    csv_file = f"{user_id}.csv"

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for item in todo_data_filtered_before:
            row_data = [item["userId"], name, item["completed"], item["title"]]
            writer.writerow(row_data)
