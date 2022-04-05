from collections import defaultdict

def averageOfLevels(root):
    # takes care of edge case
    if not root:
        return []
    # set up the queue
    averages, nodes = [], [root]
    # while there is still unexplored nodes
    while nodes:
        # for all the current level nodes, calculate
        averages.append(sum(node.val for node in nodes) / len(nodes))
        # both pop all the previous level and add their children
        for _ in range(len(nodes)):
            node = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
    return averages


'''
def averageOfLevels(root):
    sums = defaultdict(float)
    totalNodesCount = defaultdict(int)

    def dfs(node, h):
        if not node:
            return
        dfs(node.left, h + 1)
        dfs(node.right, h + 1)

        sums[h] += node.val
        totalNodesCount[h] += 1

    dfs(root, 0)
    result = []
    for i in range(len(sums)):
        result.append(sums[i] / totalNodesCount[i])
    return result
'''