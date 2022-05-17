class Node: # create new node class for linked list implementation
    def __init__(self, key, val):
      self.key, self.val = key, val # each input from the problem has a key and a value [key, value]
      self.prev = self.next = None # creating a doubly linked list for the LRU and MRU relationship

class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity # keep track of how many nodes we can have and when we are over
        self.cache = {} # map key to node, O(1) look up

        self.left, self.right = Node(0, 0), Node(0, 0) # Dummy nodes whose values wont change. But pointers will change to track LRU and MRU
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
        if key in self.cache: # we are now making the node the MRU node given its now looked up
          self.remove(self.cache[key]) # remove it from the linked list
          self.insert(self.cache[key]) # re-append it but now as the right pointer or the MRU node
          return self.cache[key].val # Return the node value back to the user
        return -1 # Not present

    def put(self, key, value):
      if key in self.cache:
        self.remove(self.cache[key])
      self.cache[key] = Node(key, value) # add the new linked list node to cache
      self.insert(self.cache[key]) # insert at the MRU as it is the most recent given its just added

      if len(self.cache) > self.cap: # we hit the capacity once adding
        # remove from the linked list and delete the LRU from the hashmap
        lru = self.left.next
        self.remove(lru)
        del self.cache[lru.key] # lru is a node so we access it through dot notation
