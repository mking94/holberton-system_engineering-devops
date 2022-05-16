#!/usr/bin/python3
"""
For a given employee ID, returns information about
their TODO list progress.
"""

import requests
import sys
if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId))
    name = user.json().get('name')
    req = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = list(filter(lambda x: x['userId'] == 2, req.json()))
    comp = list(filter(lambda x: x['completed'], todos))
    print('Employee {} is done with tasks({}/{}):'
          .format(name, len(comp), len(todos)))
    for x in list(x['title'] for x in comp):
        print('\t {}'.format(x))
