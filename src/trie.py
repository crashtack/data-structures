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
        self.next_let = []

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
            if END_OF_WORD not in self.next_let:
                self.next_let.append(Node(END_OF_WORD))
            return
        if letter not in self.next_let:
            self.next_let.append(letter)
        idx = self.next_let.index(letter)
        self.next_let[idx]._insert(word[1:])

    def _contains(self, word):
        """
        Check to see if the letter is in next.
        Passes the remaining part of the word to the next node.
        """
        try:
            letter = word[0]
        except IndexError:
            if END_OF_WORD in self.next_let:
                return True
            else:
                return False
        if letter in self.next_let:
            idx = self.next_let.index(letter)
            return self.next_let[idx]._contains(word[1:])
        else:
            return False

    def _traversal(self, word=''):
        # import pdb; pdb.set_trace()
        for node in self.next_let:
            if node.value == '$':
                yield word
            else:
                word += node.value
                node._traversal(word)


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

    def traversal(self):
        yield self.first_node._traversal()

