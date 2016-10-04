# -*- coding utf-8 -*-
"""Implementation of a quick sort."""

def additive_hash(input):
    hash_value = 0
    for char in str(input):
        hash_value += ord(char)
    return hash_value
