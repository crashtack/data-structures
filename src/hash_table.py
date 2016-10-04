# -*- coding utf-8 -*-
"""Implementation of a quick sort."""

def additive_hash2(input):
    hash_value = 0
    for char in str(input):
        hash_value += ord(char)
    return hash_value

def additive_hash(input):
    try:
        input = input.encode()
    except AttributeError:
        raise AttributeError ('Input needs to be a string.')
    hash_value = 0
    my_array = bytearray(input)
    for num in my_array:
        hash_value += num
    return hash_value

def xor_hash(input):
    try:
        input = input.encode()
    except AttributeError:
        raise AttributeError ('Input needs to be a string.')
    hash_value = 0
    my_array = bytearray(input)
    for num in my_array:
        hash_value = num ^ hash_value
    return hash_value