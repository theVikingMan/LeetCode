def countComponents(n, edges):
    # creating an adgency list where each node is the parent
        # of themselves initally
    parent = [i for i in range(n)]
    # list of ranks with 1 as the initial value
        # This is an optimization
    rank = [1] * n

    # find the root parent of the given node
    def find(n1):
        # Initially set the root parent to itself
        res = n1
        # Until our res variable finds that it has no parent == its the root parent
        while res != parent[res]:
            # path compression of setting parent to grandparent
            parent[res] = parent[parent[res]]
            # setting the current node to its parent
            res = parent[res]
        return res

    def union(n1, n2):
        # find root parents of the nodes that we want to merge
        p1, p2 = find(n1), find(n2)
        # If they already have the same parent, return immediately and indicate 0 unions made
        if p1 == p2:
            return 0

        # check how to rank. See how union find works but its unioning the
            # smaller group to the larger group and combining rank
        if rank[p2] > rank[p1]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        # 1 Lets us know that we have performed a union
        return 1

    res = n
    for n1, n2 in edges:
        res -= union(n1, n2)

    return res

print(countComponents(5, [[0,1],[1,2],[3,4]]))