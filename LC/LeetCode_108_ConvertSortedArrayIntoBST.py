class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----------- Recursive Binary Search Solution ----------- #

def sortedArrayToBST(nums):
  def helper(l, r):
    if l > r:
      return None
    m = (l + r) // 2

    parNode = TreeNode(nums[m])
    parNode.left = helper(l, m - 1)
    parNode.right = helper(m + 1, r)
    return parNode

  left, right = 0, len(nums) - 1
  return helper(left, right)

# T: O(N) -> N is length of input nums array. We have to visit all nodes
# S: O(log(n)) -> Balanced tree