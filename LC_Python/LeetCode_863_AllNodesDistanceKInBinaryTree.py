# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        # dfs preorder traversal to map each node to its parent
        def get_parent(node, parent):
            if not node:
                return
            # adjacency list to the parent
            hashmap[node] = parent
            # search the left and right passing in the recent node as the parent
            # parameter
            get_parent(node.left, node), get_parent(node.right, node)

        def search(node, distance):
            # if not what we are looking for, kill that call stack
            if not node or node.val in visited:
                return
            # Mark it has been looked at
            visited.add(node.val)
            # If we have reached a solution, add it to output counter
            if distance == k:
                answer.append(node.val)
            # BFS upwards (aka the parent), and downwards (aka the left and right node)
            for neighbour in (hashmap[node], node.left, node.right):
                search(neighbour, distance+1)

        hashmap = {}
        answer = []
        visited = set()

        get_parent(root, None)
        search(target, 0)

        return answer