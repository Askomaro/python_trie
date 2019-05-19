from trie import Trie

if __name__ == '__main__':
    words = ["book", "bookcase", "booking", "booklet", "bookshelf", "boost",
             "boot", "booth", "border", "bore", "boring", "born", "borrow"]

    trie = Trie()
    trie.insert_list(words)

    print(trie.walk_trie())
