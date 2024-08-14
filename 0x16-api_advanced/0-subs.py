#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns
    """
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.ReqestException:
        return 0
