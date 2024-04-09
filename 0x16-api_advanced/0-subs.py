#!/usr/bin/python3
''' 0-subs.py '''
import requests
import json


def number_of_subscribers(subreddit):
    ''' returns number of subscribers '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(
        subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
