# -*- coding utf-8 -*-
"""Implementation of a quick sort."""

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


class HashTable(object):
    def __init__(self, size, hash=sax_hash):
        self.size = size
        self._implemented_hashes = [add_hash, xor_hash, rot_hash, sax_hash]
        if hash in self._implemented_hashes:
            self._hash = hash
        else:
            raise ValueError('Not a correct type of hash.')

    def _hash(self, key):
        return self.hash(key)

    def set(self, key, value):
        key = self._hash(key) % self.size





