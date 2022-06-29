def postorderTraversal(root):
    res = []
    def bfs(node):
        if node:
            bfs(node.left)
            bfs(node.right)
            res.append(node.val)
    bfs(root)
    return res