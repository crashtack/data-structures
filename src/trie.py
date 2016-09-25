# -*- coding utf-8 -*-

END_OF_WORD = '$'


class Node(object):
    """Node object.  Has a value and a list of nodes that could come next."""

    def __init__(self, value=None):
        """
        Each node will contain the letter at that node and a list of
        node that come next.
        """
        self.value = value
        self.next = []

    def __eq__(self, other):
        """Allow nodes to compare and check if a letter is in next list."""
        return self.value == other

    def _insert(self, word):
        """
        Will insert a letter into the list of letters that come next.
        The remaining part of the word to the next node.
        """
        try:
            letter = Node(word[0])
        except IndexError:
            if END_OF_WORD not in self.next:
                self.next.append(Node(END_OF_WORD))
            return
        if letter not in self.next:
            self.next.append(letter)
        idx = self.next.index(letter)
        self.next[idx]._insert(word[1:])

    def _contains(self, word):
        """
        Check to see if the letter is in next.
        Passes the remaining part of the word to the next node.
        """
        try:
            letter = word[0]
        except IndexError:
            if END_OF_WORD in self.next:
                return True
            else:
                return False
        if letter in self.next:
            idx = self.next.index(letter)
            return self.next[idx]._contains(word[1:])
        else:
            return False


class Trie(object):
    """Trie class. Has an a pointer to first_node."""

    def __init__(self):
        """Initalize trie so first_node is empty."""
        self.first_node = Node()

    def insert(self, word):
        """Insert a given word to the first_node."""
        self.first_node._insert(word)

    def contains(self, word):
        """Check to see if a word starts from the first node."""
        return self.first_node._contains(word)
