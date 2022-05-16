#!/usr/bin/python3
""" Export to csv file """

import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId))
    name = user.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    task = list(filter(lambda x: x['userId'] == int(userId), todos.json()))

    with open('{}.csv'.format(userId), 'w', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for x in task:
            row = [
                str(userId), str(name), str(
                    x["completed"]), str(
                    x["title"])]
            writer.writerow(row)
