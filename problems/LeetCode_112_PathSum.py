def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    # Base case that null is initially given
    if not root:
        return False

    # converge the sum onto 0
    sum -= root.val
    # Once we hit a leaf (no left or right node) check if we have an answer in our tree
    if not root.left and not root.right:
        return sum == 0
    # If more nodes to search then search. We ONLY need ONE True to be returned back up
    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)