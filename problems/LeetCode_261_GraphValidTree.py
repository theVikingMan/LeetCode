def validTree(n, edges):
    if not n: # input validation to see if there isnt a tree
        return True

    adj = { i:[] for i in range(n)} # Create 2-way adjancy list, remember its undirected (Not a DAG)
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visited = set() # Create and find if there is a cycle
    def dfs(i, prev):
        if i in visited: # have we seen the node before in our search -> cycle
            return False

        visited.add(i) # Mark that we have seen it before

        for j in adj[i]: # search all the current node's neightbors
            if j == prev: # check if it is one we are coming from
                continue
            if not dfs(j, i): # if our recursive call found a cycle
                return False
        return True

    return dfs(0, -1) and n == len(visited) # all nodes should be connected aka visited through DFS

print(validTree(5, [[0,1],[0,2],[0,3],[1,4]]))