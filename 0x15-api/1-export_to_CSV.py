#!/usr/bin/python3
""" Export to csv file """
import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    usr_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    tds_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    user = requests.get(usr_url).json()
    todo = requests.get(tds_url).json()

    with open('{}.csv'.format(id), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for x in todo:
            row = [str(id),str(user.get("username")),str(x.get("completed")),str(x.get("completed"))]
            writer.writerow(row)
