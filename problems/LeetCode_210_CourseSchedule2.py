
def findOrder(numCourses, prerequisites):
      # Construct adj list
      adj = { i:[] for i in range(numCourses) }
      for crs, pre in prerequisites:
        adj[crs].append(pre)

      visit = {}
      res = []

      def dfs(node): # create dfs for each node
        if node in visit: # Have we already analyzed it?
          return visit[node]
        visit[node] = True # We are currently visiting it
        for nei in adj[node]:
          if dfs(nei):
            return True
        visit[node] = False
        res.append(node)

      for crs in range(numCourses):
        if dfs(crs):
          return []
      return res

print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
'''
    preMap = {i:[] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
    output = []
    # Create cycle detection set
    cycle = set()
    visit = set()
    # Travse using DFS

    def dfs(crs):
        # We have seen the node -> cycle detected
        if crs in cycle:
            return False
        # No preRecs or we are able to take the course
        if crs in visit:
            return True
        cycle.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return []
    return output
'''

