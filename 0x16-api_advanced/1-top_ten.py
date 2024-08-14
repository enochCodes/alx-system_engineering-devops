#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """
    Queries the Reddit API and returns
    """
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'user-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except requests.ReqestException:
        return (None)
