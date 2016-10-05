# -*- coding utf-8 -*-
"""Implementation of a quick sort."""

def additive_hash2(input):
    hash_value = 0
    for char in str(input):
        hash_value += ord(char)
    return hash_value

def add_hash(input):
    input = str(input).encode()
    hash_value = 0
    my_array = bytearray(input)
    for num in my_array:
        hash_value += num
    return hash_value

def xor_hash(input):
    input = str(input).encode()
    hash_value = 0
    my_array = bytearray(input)
    for num in my_array:
        hash_value = num ^ hash_value
    return hash_value

def rot_hash(input):
    input = str(input).encode()
    hash_value = 0
    my_array = bytearray(input)
    for num in my_array:
        hash_value = (hash_value << 4) ^ (hash_value >> 28) ^ num
    return hash_value


def sax_hash(input):
    input = str(input).encode()
    hash_value = 0
    my_array = bytearray(input)
    for num in my_array:
        hash_value = (hash_value << 5) + (hash_value >> 2) ^ num
    return hash_value