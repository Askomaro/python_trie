class Node(object):
    def __init__(self, is_end=False):
        self.children = {}
        self.label = {}
        self.is_full_word = is_end


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
        i = 0

        while i < len(word) and word[i] in current_node.label:
            j = 0
            index = word[i]
            label = current_node.label[index]

            while j < len(label) and i < len(word) and label[j] == word[i]:
                i += 1
                j += 1

            if j == len(label):
                current_node = current_node.children[index]
            else:
                if i == len(word):
                    ex_child = current_node.children[index]
                    new_child = Node(True)
                    remaining_label = label[j:]

                    current_node.label[index] = label[:j]
                    current_node.children[index] = new_child
                    new_child.children[remaining_label[0]] = ex_child
                    new_child.label[remaining_label[0]] = remaining_label
                else:
                    remaining_label = label[j:]
                    remaining_word = word[i:]

                    new_child = Node()
                    ex_child = current_node.children[index]

                    current_node.label[index] = label[:j]
                    current_node.children[index] = new_child

                    new_child.children[remaining_label[0]] = ex_child
                    new_child.label[remaining_label[0]] = remaining_label
                    new_child.label[remaining_word[0]] = remaining_word
                    new_child.children[remaining_word[0]] = Node(True)

                return

        if i < len(word):
            current_node.label[word[i]] = word[i:]
            current_node.children[word[i]] = Node(True)
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
        return self._get_all_words(self.root, [], "")

    def find(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        i = 0
        current_node = self.root

        while i < len(word) and word[i] in current_node.label:
            j = 0
            index = word[i]
            label = current_node.label[index]

            while j < len(label) and i < len(word):
                if word[i] != label[j]:
                    return False
                i += 1
                j += 1

            if j == len(label) and len(word) >= i:
                current_node = current_node.children[index]
            else:
                return False

        return i == len(word) and current_node.is_full_word

    def get_max_level(self):
        """
        Returns max level number.
        :rtype: int
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

        for key in node.label:
            part_word = node.label[key]
            word += part_word
            self._get_all_words(node.children[key], words, word)
            word = word.replace(part_word, "")

        return words
