class Solution(object):
    def isSubtree(self, root, subRoot):
        # a root tree can possess a nothing tree
        if not subRoot:
            return True
        # BUT a nothing root tree does NOT possess another whole tree
        if not root:
            return False

        # check initial root given
        if self.isSame(root, subRoot):
            return True

        # No we can check the left and right
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSame(self, p, q):
        if not p and not q:
            return True
        if (not p or not q) or (p.val != q.val):
            return False
        if (p and q) and (p.val == q.val):
            return (self.isSame(p.left, q.left) and self.isSame(p.right, q.right))


        return (isSame(curr, subRoot))