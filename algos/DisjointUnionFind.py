def countComponents(n, edges):
    parent = [i for i in range(n)] # All nodes are disjoint initially
    rank = [1] * n # All nodes are size of 1 initially

    def find(n1):
        res = n1
        while res != parent[res]: # while there are still parents above the current node
            parent[res] = parent[parent[res]] # path compression
            res = parent[res] # move node up to parent / grandparent
        return res

    def union(n1, n2):
        p1, p2 = find(n1), find(n2) # find parents of the pair
        if p1 == p2: # if already union'd, break
            return 0
        if rank[p2] > rank[p1]: # compare rank. Larger rank (size of grouping) will absorb the smaller group
            parent[p1] = p2 # connect smaller node to larger by making smaller node's parent the main parent of the larger group
            rank[p2] += rank[p1] # increase rank by the size of the smaller group
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        return 1 # returning that we have made a union

    res = n
    for n1, n2 in edges:
        res -= union(n1, n2)
    return res

print(countComponents(5, [[0,1],[1,2],[3,4]]))