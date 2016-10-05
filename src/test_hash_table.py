# -*- coding utf-8 -*-

import pytest
from hash_table import add_hash, xor_hash, rot_hash, sax_hash, HashTable

TYPE_OF_HASH = [add_hash, xor_hash, rot_hash, sax_hash]

# def test_add_include():
#     """test to see if hash can be included"""
#     from hash_table import add_hash


@pytest.mark.parametrize('hash_type', TYPE_OF_HASH)
def test_add_return_int(hash_type):
    """Test to see if a integer is returned from the hash function."""
    returned_val = hash_type('a')
    assert type(returned_val) is int


@pytest.mark.parametrize('hash_type', TYPE_OF_HASH)
def test_hash_one_letter(hash_type):
    """test to see if hash function will hash a single letter"""
    assert hash_type('a') == 97

@pytest.mark.parametrize('hash_type', TYPE_OF_HASH)
def test_hash_int(hash_type):
    """test to see if hash will hash a number"""
    assert hash_type(1) == 49


def test_add_two_numbers():
    """test to see if add_hash will hash a number"""
    assert add_hash('ab') == 195


def test_xor_two_numbers():
    """test to see if xor_hash will hash a string len2"""
    assert xor_hash('ab') == 3

def test_xor_two_numbers2():
    """test to see if xor_hash will hash a string len2"""
    assert xor_hash('op') == 31


def test_initialize_table():
    """test to see if hash table initializes with a size"""
    ht = HashTable(1024)
    assert ht.size == 1024

def test_initialize_hash():
    """test to see if hash table initializes with default hash."""
    ht = HashTable(1024)
    assert ht._hash == sax_hash

def test_initialize_hash_specified():
    """test to see if hash table initializes with specified hash."""
    ht = HashTable(1024, rot_hash)
    assert ht._hash == rot_hash

def test_initialize_hash_specified_not_in_list():
    """test to see if hash table initializes with specified hash."""
    with pytest.raises(ValueError):
        ht = HashTable(1024, 'the_hash')


def test_check_hash_function():
    ht = HashTable(1024)
    assert ht._hash('key') == sax_hash('key')


def test_check_hash_function_specified():
    ht = HashTable(1024, add_hash)
    assert ht._hash('key') == add_hash('key')



