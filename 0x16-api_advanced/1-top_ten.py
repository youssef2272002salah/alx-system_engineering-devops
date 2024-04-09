#!/usr/bin/python3
''' 0-subs.py '''
import requests


def top_ten(subreddit):
    ''' returns number of subscribers '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(
        subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    params = {"limit": 10}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)
    try:

        data = response.json().get("data").get("children")
        for child in data:
            print(child.get("data").get("title"))
    except KeyError:
        print("None")
