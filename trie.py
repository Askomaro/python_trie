from collections import defaultdict


class Node(object):
    def __init__(self):
        self.children = defaultdict(Node)
        self.label = ''
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

        # for char in word:
        #     current_node = current_node.children[char]
        i = 0
        while i < len(word):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
                i += 1
                if word[i] == current_node.label[i]:
                    i += 1

        if i < len(word):
            current_node = current_node.children[word[i]]
            current_node.is_full_word = True
            current_node.label = word
        else:
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

    def get_max_level(self):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        max_level, _ = self._get_max_level(self.root, 0, 0)
        return max_level

    def _get_max_level(self, node, counter, max_counter):
        for key in node.children:
            counter += 1
            max_counter, counter = self._get_max_level(node.children[key], counter, max_counter)
            counter -= 1

        if counter > max_counter:
            max_counter = counter

        return max_counter, counter

    def _get_all_words(self, node, words, word):
        if node.is_full_word:
            words.append(word)

        for key in node.children:
            word += key
            self._get_all_words(node.children[key], words, word)
            word = word[:-1]

        return words
