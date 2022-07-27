def largestBSTSubtree(root):
    def dfs(node):
        if not node:
            return 0, float("inf"), float("-inf")

        l_n, l_min, l_max = dfs(node.left)
        r_n, r_min, r_max = dfs(node.right)

        if l_max < node.val < r_min:
            return l_n + r_n + 1, min(l_min, node.val), max(r_max, node.val)
        else:
            return max(l_n, r_n), float("-inf"), float("inf")

    return dfs(root)[0]