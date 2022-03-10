import pprint

import requests


def request_to_api():
    """
    request to api https://randomuser.me/
    return: dict users
    """
    url = f'https://randomuser.me/api/?results=100&gender=male'
    return requests.get(url).json()


data = request_to_api()

print((data["results"][1]['name']))
pprint.pprint(data)

