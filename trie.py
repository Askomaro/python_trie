from collections import defaultdict


class Node(object):
    def __init__(self):
        self.ref_nodes = defaultdict(Node)
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
            current_node = current_node.ref_nodes[char]

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

    def _get_all_words(self, node, words, word):
        if node.is_full_word:
            words.append(word)
            # word = ''

        for key in node.ref_nodes:
            word += key
            print(key)
            self._get_all_words(node.ref_nodes[key], words, word)

        return words
