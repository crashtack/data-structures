# -*- coding utf-8 -*-

import pytest
from hash_table import add_hash, xor_hash, rot_hash, sax_hash, HashTable

TYPE_OF_HASH = [add_hash, xor_hash, rot_hash, sax_hash]
STRING_HASH = ['add_hash', 'xor_hash', 'rot_hash', 'sax_hash']

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
    """test to see if hash will have an attribute error with an int"""
    with pytest.raises(AttributeError):
        hash_type(1)


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
    ht = HashTable(10)
    assert ht.size == 10

def test_initialize_hash():
    """test to see if hash table initializes with default hash."""
    ht = HashTable(10)
    assert ht._hash_type == sax_hash

def test_initialize_hash_specified():
    """test to see if hash table initializes with specified hash."""
    ht = HashTable(10, 'rot_hash')
    assert ht._hash_type == rot_hash

def test_initialize_hash_specified_not_in_list():
    """test to see if hash table initializes with specified hash."""
    with pytest.raises(ValueError):
        ht = HashTable(10, 'the_hash')


def test_initialize_hash_buckets_empty():
    """test to see if hash table initializes with specified hash."""
    ht = HashTable(10)
    for i in range(10):
        assert ht.bucket[i] == []


def test_check_hash_function():
    """check the sax hash function"""
    ht = HashTable(10)
    assert ht._hash('key') == sax_hash('key')


def test_check_hash_function_specified():
    """check the use of the add_hash function"""
    ht = HashTable(10, 'add_hash')
    assert ht._hash('key') == add_hash('key')


def test_set_one_item():
    """test one item in a hash table"""
    table_size = 100
    ht = HashTable(table_size)
    ht.set('elvis', 'singer')
    key = sax_hash('elvis') % table_size
    assert ht.bucket[key] == [('elvis', 'singer')]


def test_set_one_item_all_other_buckets_still_empty():
    """tests that for 1 item i a hash, the rest are empty"""
    table_size = 100
    ht = HashTable(table_size)
    ht.set('elvis', 'singer')
    key = sax_hash('elvis') % table_size
    ht.bucket[key] == [('elvis', 'singer')]
    for i in range(table_size):
        if i != key:
            assert len(ht.bucket[i]) == 0


def test_set_two_items_collision():
    """test collision handling"""
    table_size = 100
    ht = HashTable(table_size, 'add_hash')
    ht.set('elvis', 'singer')
    ht.set('lives', 'yup')
    key = add_hash('elvis') % table_size
    assert len(ht.bucket[key]) == 2


def test_set_int():
    """test to see if hash table will raise an error without a string."""
    ht = HashTable(10)
    with pytest.raises(KeyError):
        ht.set(1, 'value')


def test_get_one_item():
    """test retreaval of one item"""
    table_size = 100
    ht = HashTable(table_size)
    ht.set('elvis', 'singer')
    assert ht.get('elvis') == 'singer'


def test_get_two_items_collision():
    """get i collided item out"""
    table_size = 100
    ht = HashTable(table_size, 'add_hash')
    ht.set('elvis', 'singer')
    ht.set('lives', 'yup')
    assert ht.get('elvis') == 'singer'
    assert ht.get('lives') == 'yup'


def test_get_item_not_in_table():
    """test a error is raised for item not in the table"""
    table_size = 100
    ht = HashTable(table_size)
    ht.set('elvis', 'singer')
    with pytest.raises(KeyError):
        ht.get('lives')


@pytest.mark.parametrize('hash_type', STRING_HASH)
def test_hash_full_table_retrieves_val(hash_type):
    """test to see if loaded hash table will return correct value."""
    from hash_table import ExampleHashTable
    ht = ExampleHashTable(hash_type)
    assert ht.get('aardvark') == 'aardvark'
    assert ht.get('table') == 'table'
