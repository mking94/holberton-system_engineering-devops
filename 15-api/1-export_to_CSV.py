#!/usr/bin/python3
import requests
import sys
"""For a given employee ID, returns information about
their TODO list progress """
if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId))
    name = user.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    task = list(filter(lambda x: x['userId'] == 2, todos.json()))

    f = open("{}.csv".format(sys.argv[1]), "w")
    for x in task:
        f.write(
            '"{}","{}","{}"\n'.format(
                x['userId'],
                x['completed'],
                x['title']))
    f.close()
