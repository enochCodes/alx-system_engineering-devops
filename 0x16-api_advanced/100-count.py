#!/usr/bin/python3

import requests


def count_words(subreddit, word_list, after='', word_count={}):
    """Recursively queries the Reddit API and counts keywords in titles."""
    # Base URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False
                )

        if response.status_code != 200:
            return

        # Parse the response JSON
        data = response.json()
        children = data.get('data', {}).get('children', [])

        # Initialize word count dictionary
        if not word_count:
            word_count = {word.lower(): 0 for word in word_list}

        # Iterate over the titles of hot posts
        for child in children:
            title = child.get('data', {}).get('title', '').lower().split()
            for word in title:
                if word in word_count:
                    word_count[word] += 1

        # Handle pagination
        after = data.get('data', {}).get('after')
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            # Sort and print the results
            sorted_word_count = sorted(
                    word_count.items(), key=lambda x: (-x[1], x[0])
                    )
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")

    except requests.RequestException as e:
        return


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
