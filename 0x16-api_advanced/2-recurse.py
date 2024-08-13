#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[]):
    """Recursively queries the reddit api"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'user-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}

    if after is not None:
        params['after'] = after
    try:
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False
                )
        if response.status_code == 200:
            data = response.json()
            children = data.get('data', {}).get('children', [])
            for child in children:
                hot_list.append(child.get('data', {}).get('title'))

            after = data.get('data', {}).get('after')
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return host_list
        else:
            return (None)
    except requests.RequestException:
        return (None)
