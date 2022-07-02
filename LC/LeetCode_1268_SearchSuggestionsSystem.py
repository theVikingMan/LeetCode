class TrieNode:
  def __init__(self):
    self.children = {}
    self.words = []
    self.endOfWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode() # Think blank starting point to any char path

  def insert(self, word: str) -> None:
    curr = self.root

    for c in word:
      if c not in curr.children:
        curr.children[c] = TrieNode()
      curr.children[c].words.append(word)
      curr = curr.children[c] # node already exists for the character
    curr.endOfWord = True


  def search(self, word: str) -> bool:
    curr = self.root

    for c in word:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    return curr.endOfWord


  def startsWith(self, prefix: str) -> bool:
    curr = self.root

    for c in prefix:
      if c not in curr.children:
        return []
      curr = curr.children[c]
    return curr

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
      Try = Trie()
      res = []
      products.sort()

      for prod in products:
        Try.insert(prod)

      for i, c in enumerate(searchWord):
        node = Try.startsWith(searchWord[:i+1])
        if not node:
          res.append([])
        else:
          res.append(node.words[:3])
      return res
