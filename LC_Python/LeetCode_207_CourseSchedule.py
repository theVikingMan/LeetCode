def findOrder(numCourses, prerequisites):

      # construct shell of adj list
      adj = { i:[] for i in range(numCourses) }
      # add the needed items to use the parent item
      for crs, pre in prerequisites:
        adj[crs].append(pre)

      visit = {}

      # create dfs for each node
      def dfs(node):
        if node in visit:
          return visit[node]
        visit[node] = True
        for nei in adj[node]:
          if dfs(nei):
            return True
        visit[node] = False

      # Loop over all nodes and run DFS on them
      for crs in range(numCourses):
        if dfs(crs):
          return False

      return True

print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
# --------- Correct but slighly different way -------- #
'''
    # Create agency list
    preMap = {i:[] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    # Create cycle detection set
    visit = set()

    # Travse using DFS. This creates a stack but not the data stack, a call stack
    # The call stack operates the same way
    def dfs(crs):
        # Base case: We have seen the node -> cycle detected
        if crs in visit:
            return False

        # Base case: No preRecs or we are able to take the course
        if preMap[crs] == []:
            return True

        # Add the current node to the cycle detection variable
        # Note that we can look at a node multiple times but
        # it can't be in the same DFS search
        visit.add(crs)

        # check all neighbors
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        # clean up so we can run DFS on other nodes w/o
        # having false positives for cycle detection
        visit.remove(crs)
        # Indicating that we can take the course
        preMap[crs] = []
        return True

    # Check all nodes as some might not be connected -> think islands
    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True
'''

