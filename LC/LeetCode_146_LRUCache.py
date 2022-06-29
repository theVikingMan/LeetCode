
class Node: # creating a doubly linked list for the LRU and MRU relationship
    def __init__(self, key, val):
      self.key, self.val = key, val
      self.prev = self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity # keep track of how many nodes we can have and when we are over
        self.cache = {} # map key to node (pointers to nodes)
        self.left, self.right = Node(0, 0), Node(0, 0) # Node pointers to track LRU and MRU
        self.left.next, self.right.prev = self.right, self.left # point to the opposite pointers

    # HELPER FUNCTIONS FOR GET FUNCTION
    # ----------------------------------
    def remove(self, node): # remove node from list
      # node will be the middle node that we want to delete
      prev, nxt = node.prev, node.next
      prev.next, nxt.prev = nxt, prev


    def insert(self, node): # insert at right most position, just before the right pointer
      prev, nxt = self.right.prev, self.right
      prev.next = nxt.prev = node
      node.next, node.prev = nxt, prev

    def get(self, key):
        if key in self.cache: # we are now making the node the MRU node
          self.remove(self.cache[key]) # remove it from the linked list
          self.insert(self.cache[key]) # re-append it but now as the right pointer or the MRU node
          return self.cache[key].val # Return the node value back to the user
        return -1


    def put(self, key, value):
      if key in self.cache:
        self.remove(self.cache[key])
      self.cache[key] = Node(key, value)
      self.insert(self.cache[key])

      if len(self.cache) > self.cap:  # remove from the linked list and delete the LRU from the hashmap
        lru = self.left.next
        self.remove(lru)
        del self.cache[lru.key]
