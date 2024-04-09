#!/usr/bin/python3
''' 0-subs.py '''
import requests
import json


def number_of_subscribers(subreddit):
    ''' returns number of subscribers '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(
        subreddit)  # Corrected URL
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()
    # data = json.dumps(data["data"], indent=4)
    # print (data)
    if response.status_code == 404:
        return 0
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
