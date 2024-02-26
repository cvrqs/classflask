import argparse
import sys
import requests
import json

parser = argparse.ArgumentParser()

parser.add_argument('host', metavar='host', nargs='?',
                    type=str)

parser.add_argument('port', metavar='port', nargs='?',
                    type=str)

parser.add_argument('dates', metavar='dates', nargs='+',
                    type=str)

parser.add_argument('--coeff', metavar='coeff', nargs='?',
                    type=int, default=2, help='любитель кукл')

parser.add_argument('--subtract', metavar='subtract', nargs='?',
                    type=int, default=[], help='любитель кукл')

args = parser.parse_args()

host = args.host
port = args.port
dates = args.dates
print(dates)

coeff = args.coeff

def get_api(server, port):
    sp = []


    url = f"http://{server}:{port}"

    response = requests.get(url)
    json_answer = response.json()
    print(json_answer)
    if coeff:

        for i in range(len(dates)):
            c = 0
            if dates[i] in json_answer:

                for j in json_answer[dates[i]]:

                    if j % 2 != 0:
                        j *= coeff
                        c += j
                    else:
                        c += j
            sp.append(c)
    print(c)

get_api(host, port)