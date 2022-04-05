def validTree(n, edges):
    # input validation to see if there isnt a tree
    if not n:
        return True

    # Create adjancy list, remember its undirected so
        # both nodes are neighbors of eachother
    adj = { i:[] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    # Create and find if there is a cycle
    visited = set()
    def dfs(i, prev):
        # have we seen the node before in our search -> cycle
        if i in visited:
            return False

        # Mark that we have seen it before
        visited.add(i)

        # search all the current node's neightbors
        for j in adj[i]:
            # check if it is one we are coming from
            if j == prev:
                continue
            # if our recursive call found a cycle
            if not dfs(j, i):
                return False
        return True

    return dfs(0, -1) and n == len(visited)

print(validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))