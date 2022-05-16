#!/usr/bin/python3
import requests
import sys
""" Export to csv file """
if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId))
    name = user.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    task = list(filter(lambda x: x['userId'] == int(userId), todos.json()))

    f = open("{}.csv".format(userId), "w")
    for x in task:
        f.write(
            '"{}","{}","{}","{}"\n'.format(
                x['userId'],
                name,
                x['completed'],
                x['title']))
    f.close()
