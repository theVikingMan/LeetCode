
def maxDepth(root):
    # base case if root is none -> see if its a max
    if not root:
        return 0
    return 1 +  max(self.maxDepth(root.left), self.maxDepth(root.right))