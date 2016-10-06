# -*- coding utf-8 -*-
"""Implementation of a quick sort."""

WORD_LIST = '/usr/share/dict/words'


def add_hash(input):
    """additive hash"""
    input = input.encode()
    hash_value = 0
    my_array = bytearray(input)
    for num in my_array:
        hash_value += num
    return hash_value


def xor_hash(input):
    """binary xor hash"""
    input = input.encode()
    hash_value = 0
    my_array = bytearray(input)
    for num in my_array:
        hash_value = num ^ hash_value
    return hash_value


def rot_hash(input):
    """rotating hash"""
    input = input.encode()
    hash_value = 0
    my_array = bytearray(input)
    for num in my_array:
        hash_value = (hash_value << 4) ^ (hash_value >> 28) ^ num
    return hash_value


def sax_hash(input):
    """saxiphone hash"""
    input = input.encode()
    hash_value = 0
    my_array = bytearray(input)
    for num in my_array:
        hash_value = (hash_value << 5) + (hash_value >> 2) ^ num
    return hash_value


class HashTable(object):
    def __init__(self, size, hash_type='sax_hash'):
        """initialize the hash table"""
        self.size = size
        self._implemented_hashes = {
            'add_hash': add_hash,
            'xor_hash': xor_hash,
            'rot_hash': rot_hash,
            'sax_hash': sax_hash
        }
        if hash_type in self._implemented_hashes:
            self._hash_type = self._implemented_hashes[hash_type]
        else:
            raise ValueError('Not a correct type of hash.')
        self.bucket = []
        for i in range(self.size):
            self.bucket.append([])

    def _hash(self, key):
        """hash the value of the key with the given hash"""
        return self._hash_type(key)

    def set(self, key, value):
        """add something to the white table"""
        try:
            hashed_key = self._hash(key) % self.size
        except AttributeError:
            raise KeyError('Key value must be a string')
        if value not in self.bucket[hashed_key]:
            self.bucket[hashed_key].append((key, value))

    def get(self, key):
        """get an item from the table"""
        hashed_key = self._hash(key) % self.size
        for item in self.bucket[hashed_key]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)


class ExampleHashTable(HashTable):
    def __init__(self, hash_type='sax_hash'):
        HashTable.__init__(self, 1000000, hash_type)
        self.load_dictionary()

    def load_dictionary(self):
        """load the dictionary from the os"""
        word_list_file = open(WORD_LIST, 'r')

        for line in word_list_file:
            word = line.rstrip('\n')
            self.set(word, word)

        word_list_file.close()
