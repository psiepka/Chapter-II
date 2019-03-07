#!/usr/bin/env python
"""
Secound task in chapter II
"""
import requests


URL_RAW_DATA = 'https://pastebin.com/raw/azc6e9fD'
REQ = requests.get(URL_RAW_DATA)
DATA_JSON = REQ.json()

def search_dict(x_data):
    """Function searching in data integers and returns sum of them.
    Arguments:
        x {dict} -- dictonary with data
    Returns:
        [int] -- sum of integers in data
    """
    result = 0
    for k_x, v_x in x_data.items():
        if isinstance(v_x, int):
            result += v_x
        elif isinstance(v_x, dict):
            result += search_dict(v_x)
        elif isinstance(v_x, (tuple,list,set)):
            result += search_list(v_x)
    return result

def search_list(xyz):
    """Function searching in data integers and returns sum of them.
    Arguments:
        x {list} -- list with data
    Returns:
        [int] -- sum of integers in data
    """
    res = 0
    for x_item in xyz:
        if isinstance(x_item, int):
            res += x_item
        elif isinstance(x_item, (tuple,list,set)):
            res += search_list(x_item)
        elif isinstance(x_item, dict):
            res += search_dict(x_item)
    return res

def search_json(json):
    """Function searching in data integers and returns sum of them.
    Arguments:
        x {json} -- list with data
    Returns:
        [int] -- sum of integers in data
    """
    result = 0
    if isinstance(json, int):
        result += json
    elif isinstance(json, (tuple,list,set)):
        result += search_list(json)
    elif isinstance(json, dict):
        result += search_dict(json)
    return result

print(search_json(DATA_JSON))
