
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(self, root, k):
    stack = [] # start off with empty stack. Stack is another way to DFS
    curr = root
    n = 0

    while curr or stack:
        while curr: # traverse left as far as possible
            stack.append(curr) # if still more left nodes, add it to the stack to then search later in that order
            curr = curr.left
        curr = stack.pop() # search the node with the most recent Null left or checked side
        n += 1 # converge on k as we have seen another smallest node
        if n == k:
            return curr.val
        curr = curr.right # no more left, check right now which will run the left most process again