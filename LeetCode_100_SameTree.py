# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        
        # p and q are both None
        if not p and not q:
            return True
        
        # one of p and q is None
        if not q or not p:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)



# Modified way from LeetCode_101
'''
class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isMirror(p.left, q.left) and self.isMirror(q.right, p.right)

    def isMirror(self, p_derv, q_derv):
        if p_derv is None and q_derv is None:
            return True
        if p_derv is None or q_derv is None:
            return False

        if p_derv.val == q_derv.val:
            outPair = self.isMirror(p_derv.left, q_derv.left)
            inPiar = self.isMirror(p_derv.right, q_derv.right)
            return outPair and inPiar
        else:
            return False
'''