# -*- coding utf-8 -*-

import pytest

def test_add_include():
    """test to see if additive_hash can be included"""
    from hash_table import add_hash

def test_add_return_int():
    """Test to see if a integer is returned from the hash function."""
    from hash_table import add_hash
    returned_val = add_hash('a')
    assert type(returned_val) is int

def test_add_one_letter():
    """test to see if add_hash will hash a single letter"""
    from hash_table import add_hash
    assert add_hash('a') == 97

def test_add_int():
    """test to see if add_hash will raise an error if an int is given"""
    from hash_table import add_hash
    assert add_hash(1) == 49

def test_add_two_numbers():
    """test to see if add_hash will hash a number"""
    from hash_table import add_hash
    assert add_hash('ab') == 195

def test_xor_include():
    """test to see if xor_hash can be included"""
    from hash_table import xor_hash

def test_xor_return_int():
    """Test to see if a integer is returned from the hash function."""
    from hash_table import xor_hash
    returned_val = xor_hash('a')
    assert type(returned_val) is int

def test_xor_one_letter():
    """test to see if xor_hash will hash a single letter"""
    from hash_table import xor_hash
    assert xor_hash('a') == 97

def test_xor_int():
    """test to see if xor_hash will raise an error if an int is given"""
    from hash_table import xor_hash
    assert xor_hash(1) == 49

def test_xor_two_numbers():
    """test to see if xor_hash will hash a number"""
    from hash_table import xor_hash
    assert xor_hash('ab') == 3

def test_xor_two_numbers2():
    """test to see if xor_hash will hash a number"""
    from hash_table import xor_hash
    assert xor_hash('op') == 31

def test_rot_include():
    """test to see if rot_hash can be included"""
    from hash_table import rot_hash

def test_rot_return_int():
    """Test to see if a integer is returned from the hash function."""
    from hash_table import rot_hash
    returned_val = rot_hash('a')
    assert type(returned_val) is int

def test_rot_one_letter():
    """test to see if rot_hash will hash a single letter"""
    from hash_table import rot_hash
    assert rot_hash('a') == 97

def test_rot_int():
    """test to see if rot_hash will raise an error if an int is given"""
    from hash_table import rot_hash
    assert rot_hash(1) == 49

def test_rot_two_numbers():
    """test to see if rot_hash will hash a number"""
    from hash_table import rot_hash
    assert rot_hash('ab') == 3

def test_rot_two_numbers2():
    """test to see if rot_hash will hash a number"""
    from hash_table import rot_hash
    assert rot_hash('op') == 31

