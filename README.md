# Realization of compressed prefix tree (compact trie/ trie tree) using Python
Structure:

trie.py - trie data structure, with realization of a trie node along with trie functionality as:
- get_max_level - the longest way from start to end node
- walk_tree - go through tree and return all the words or yield each of them
- find - return True if given word exists in your tree

Complexity:

The amount of time it takes to create a trie is tied directly to how many words/keys the trie contains, 
and how long those keys could potentially be. The worst-case runtime for creating a trie is 
a combination of m, the length of the longest key in the trie, and n, the total number of keys in the trie. 
Thus, the worst case runtime of creating a trie is O(mn).

Insert operation:
- Time complexity : O(a), where a is the key length.
- Space complexity : O(m). In the worst case newly inserted key doesn't share a prefix 
with the the keys already inserted in the trie. We have to add mm new nodes, which takes us O(m) space.

The time complexity of searching, inserting from a trie depends on the length of the word a that’s being searched for, 
inserted making the runtime of these operations O(a). 
Of course, for the longest word in the trie, inserting, searching
will take more time and memory than for the shortest word in the trie.

Search operation:
- Time complexity : O(a)
- Space complexity : O(1)


Compressed trie tree is same as that of a regular trie tree. 
In terms of memory, a compressed trie tree uses very few amount of nodes which gives a huge memory advantage 
especially for long strings with long common prefixes.


Resources:
- https://medium.com/basecs/compressing-radix-trees-without-too-many-tears-a2e658adb9a0
- https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014
- https://en.wikipedia.org/wiki/Trie
- http://theoryofprogramming.com/2016/11/15/compressed-trie-tree/