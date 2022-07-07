class TrieNode:
    def __init__(self):
        self.children = {}
        # self.words = 0
        self.endOfWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            # cur.words += 1
        cur.endOfWord = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord


    def startsWith(self, prefix):
        cur = self.root
        # count = 0
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
            # if cur.endOfWord:
            #   count += cur.words
        return True

# Your Trie object will be instantiated and called as such:
# word = 'apple'
# prefix = 'app'

# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


