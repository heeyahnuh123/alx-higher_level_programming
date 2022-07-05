#!/usr/bin/python3
"""
Module 6-from_json_string
Contains function that returns python data structure from JSON string
"""


def from_json_string(my_str):
    """Returns python data structure from JSON string
    Args:
        my_str: json string rep
    Return:
        python object
    """
    import json

    return json.loads(my_str)
