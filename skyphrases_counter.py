#!/usr/bin/env python
"""
First task in chapter II
"""

from collections import Counter
import requests


URL_RAW_DATA = 'https://pastebin.com/raw/3u4QViN8'

def count_skyphrases(url_raw_data):
    """Function to count skyphrases

    Arguments:
        raw_data {[string]} -- website url contain raw data,
            (every skypharse are in new line [seperate by '\r\n'])

    Returns:
        [int] -- return how many skypharses are valid in raw data
    """

    req = requests.get(url_raw_data)
    data = req.text.split('\r\n')
    valid_count = 0
    for d_line in data:
        validate_data = d_line.split(' ')
        result = set(Counter(validate_data).values())
        if result == {1}:
            valid_count += 1
    return valid_count

count_skyphrases(URL_RAW_DATA)
print(count_skyphrases(URL_RAW_DATA))
