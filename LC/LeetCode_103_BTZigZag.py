import collections

class Solution(object):
    def zigzagLevelOrder(self, root):
        q = collections.deque([root])
        output = []

        while q:
            to_add = [] # holds each level's nodes
            for _ in range(len(q)): # Loop through all the nodes in that most recent level
                node = q.popleft()
                if node:
                    to_add.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if to_add:
                # Heres the magic, reverse if odd row
                output.append(to_add if len(output) % 2 == 0 else to_add[::-1])
        return output