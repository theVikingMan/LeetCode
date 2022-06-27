class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot: # a root tree can possess a nothing tree
            return True
        if not root: # BUT a nothing root tree does NOT possess another whole tree
            return False
        if self.isSame(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) # check the left and right

    def isSame(self, p, q):
        if not p and not q:
            return True
        if (not p or not q) or (p.val != q.val):
            return False
        if (p and q) and (p.val == q.val):
            return (self.isSame(p.left, q.left) and self.isSame(p.right, q.right))