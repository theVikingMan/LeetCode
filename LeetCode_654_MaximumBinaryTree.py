# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        # Find max num, find its index, create node to then
        # split its left and right side
        maxNum = max(nums)
        maxIdx = nums.index(maxNum)
        root = TreeNode(maxNum)

        def helper(array):
            if len(array) == 0:
                return None
            # Find max num, find its index, create node to then
            # split its left and right side
            maxSubNum = max(array)
            maxSubIdx = array.index(maxSubNum)
            rootSub = TreeNode(maxSubNum)
            # Recursivly send each half to be broken down
            rootSub.left = helper(array[:maxSubIdx])
            rootSub.right = helper(array[maxSubIdx+1:])
            return rootSub

        root.left = helper(nums[:maxIdx])
        root.right = helper(nums[maxIdx+1:])
        return root