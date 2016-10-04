# -*- coding utf-8 -*-
import types

def test_include():
    """Test that Trie can be included."""
    from trie import Trie

def test_trie_init():
    from trie import Trie
    trie = Trie()
    assert trie.first_node.value is None

def test_trie_insert_one_letter_word():
    from trie import Trie
    trie = Trie()
    trie.insert('a')
    assert 'a' in trie.first_node.next_let

def test_trie_insert_two_letter_word_first_letter():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    assert 'a' in trie.first_node.next_let

def test_trie_insert_two_letter_word_second_letter():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    assert 't' in trie.first_node.next_let[0].next_let

def test_trie_insert_two_words():
    from trie import Trie
    trie = Trie()
    trie.insert('a')
    trie.insert('at')
    assert 't' in trie.first_node.next_let[0].next_let

def test_trie_insert_two_words_one_root_count():
    from trie import Trie
    trie = Trie()
    trie.insert('a')
    trie.insert('at')
    assert len(trie.first_node.next_let) == 1

def test_trie_insert_two_words_two_root_count():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    trie.insert('be')
    assert len(trie.first_node.next_let) == 2

def test_trie_insert_two_words_leaf_value():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    trie.insert('be')
    assert 't' in trie.first_node.next_let[0].next_let

def test_trie_insert_two_words_leaf_value2():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    trie.insert('be')
    assert 'e' in trie.first_node.next_let[1].next_let

def test_word_stop_charicter():
    from trie import Trie
    trie = Trie()
    trie.insert('a')
    assert '$' in trie.first_node.next_let[0].next_let

def test_contains_one_letter_word():
    from trie import Trie
    trie = Trie()
    trie.insert('a')
    assert trie.contains('a')

def test_contains_two_letter_word():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    assert trie.contains('at')

def test_contains_long_word():
    from trie import Trie
    trie = Trie()
    trie.insert('humanitarian')
    assert trie.contains('humanitarian')

def test_contains_doesnt_contain_substring():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    assert not trie.contains('a')

def test_contains_doesnt_contain_word():
    from trie import Trie
    trie = Trie()
    trie.insert('attack')
    assert not trie.contains('attic')

def test_trie_load():
    from trie import Trie
    trie = Trie()
    new_list = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
    trie.load(new_list)
    for item in new_list:
        assert trie.contains(item)

def test_trie_load_not_in_list():
    from trie import Trie
    trie = Trie()
    new_list = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
    trie.load(new_list)
    assert not trie.contains('fin')

def test_traversal_returns_generator():
    from trie import Trie
    trie = Trie()
    output = trie.traversal()
    assert isinstance(output, types.GeneratorType)

def test_traversal_returns_token_one_letter_word():
    from trie import Trie
    trie = Trie()
    trie.insert('a')
    token_list = []
    for token in trie.traversal():
        token_list.append(token)
        # import pdb; pdb.set_trace()
    assert 'a' in token_list

def test_traversal_returns_token_two_letter_word():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    token_list = []
    for token in trie.traversal():
        token_list.append(token)
    assert 'at' in token_list

