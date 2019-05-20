from collections import defaultdict


class Node(object):
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_full_word = False


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into a trie
        :type word: str
        :rtype: void
        """
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]

        current_node.is_full_word = True

    def insert_list(self, words):
        """
        Inserts a word into a trie
        :type words: list of str
        :rtype: void
        """
        for word in words:
            self.insert(word)

    def walk_trie(self):
        """
        Finds all words from a trie
        :rtype: list of str
        """

        return self._get_all_words(self.root, [], '')

    def find(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_full_word

    def get_max_level(self, counter):
        curr = self.root

    def _get_all_words(self, node, words, word):
        if node.is_full_word:
            words.append(word)

        for key in node.children:
            word += key
            self._get_all_words(node.children[key], words, word)
            word = word[:-1]

        return words
