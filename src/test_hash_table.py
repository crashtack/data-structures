# -*- coding utf-8 -*-

import pytest

def test_include():
    """test to see if additive_hash can be included"""
    from hash_table import additive_hash

def test_return_int():
    """Test to see if a integer is returned from the hash function."""
    from hash_table import additive_hash
    returned_val = additive_hash('a')
    assert type(returned_val) is int

def test_one_letter():
    """test to see if additive_hash will hash a single letter"""
    from hash_table import additive_hash
    assert additive_hash('a') == 97

def test_int():
    """test to see if additive_hash will raise an error if an int is given"""
    from hash_table import additive_hash
    with pytest.raises(AttributeError):
        additive_hash(1) == 49

def test_two_numbers():
    """test to see if additive_hash will hash a number"""
    from hash_table import additive_hash
    assert additive_hash('ab') == 195

