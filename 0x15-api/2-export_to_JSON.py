#!/usr/bin/python3
"""
    Python script that, exports data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    usr_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    tds_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    user = requests.get(usr_url).json()
    task = requests.get(tds_url).json()

    with open('{}.json'.format(id), 'w') as f:
        tasks = []
        for x in task:
            tasks.append({"task": x.get("title"),
                          "completed": x.get("completed"),
                          "username": user.get("username")})
        data = {"{}".format(id): tasks}
        json.dump(data, f)
