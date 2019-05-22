from trie import Trie

if __name__ == '__main__':
    words = ["book", "bookcase", "booking", "booklet", "bookshelf", "boost",
             "boot", "booth", "border", "bore", "boring", "born", "borrow"]

    trie = Trie()
    trie.insert_list(words)

    print(trie.walk_trie())
    print(trie.find('book'))
    print(trie.find('booklet'))
    print(trie.find('boo'))
    print(trie.find('bor'))

    print(trie.get_max_level())
