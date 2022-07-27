
def findMinHeightTrees(n, edges):

    # edge cases
    if n <= 2:
        return [i for i in range(n)]

    # Build the graph with the adjacency list
    neighbors = [set() for i in range(n)]
    for start, end in edges:
        neighbors[start].add(end)
        neighbors[end].add(start)

    # Initialize the first layer of leaves
    # Leaf = node with 1 connection
    leaves = []
    for i in range(n):
        if len(neighbors[i]) == 1:
            leaves.append(i)

    # Trim the leaves until reaching the centroids
    remaining_nodes = n
    while remaining_nodes > 2: # at most 2 final leafs
        remaining_nodes -= len(leaves)
        new_leaves = []
        # remove the current leaves along with the edges other nodes are connected to them
        while leaves:
            leaf = leaves.pop()
            # Grab a connected node to the leaf in the graph
            neighbor = neighbors[leaf].pop()
            # remove the current leaf from all other node connections
            neighbors[neighbor].remove(leaf)
            # If found a new leaf or made a new leaf, add it
            if len(neighbors[neighbor]) == 1:
                new_leaves.append(neighbor)

        # prepare for the next round
        leaves = new_leaves

    # The remaining nodes are the centroids of the graph
    return leaves

print(findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))