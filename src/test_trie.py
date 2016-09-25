# -*- coding utf-8 -*-

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
    assert 'a' in trie.first_node.next

def test_trie_insert_two_letter_word_first_letter():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    assert 'a' in trie.first_node.next

def test_trie_insert_two_letter_word_second_letter():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    assert 't' in trie.first_node.next[0].next

def test_trie_insert_two_words():
    from trie import Trie
    trie = Trie()
    trie.insert('a')
    trie.insert('at')
    assert 't' in trie.first_node.next[0].next

def test_trie_insert_two_words_one_root_count():
    from trie import Trie
    trie = Trie()
    trie.insert('a')
    trie.insert('at')
    assert len(trie.first_node.next) == 1

def test_trie_insert_two_words_two_root_count():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    trie.insert('be')
    assert len(trie.first_node.next) == 2

def test_trie_insert_two_words_leaf_value():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    trie.insert('be')
    assert 't' in trie.first_node.next[0].next

def test_trie_insert_two_words_leaf_value2():
    from trie import Trie
    trie = Trie()
    trie.insert('at')
    trie.insert('be')
    assert 'e' in trie.first_node.next[1].next

def test_word_stop_charicter():
    from trie import Trie
    trie = Trie()
    trie.insert('a')
    assert '$' in trie.first_node.next[0].next

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
