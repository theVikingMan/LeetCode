def solution(numCourses, prerequisites):
  # STEP 1: Make the graph adjency list
      # construct shell of adj list
      adj = { i:[] for i in range(numCourses) }
      # add the needed items to use the parent item
      for crs, pre in prerequisites:
        adj[crs].append(pre)

      visit = {} # track current visiting nodes and nodes we have analyzed already

# STEP 2: Create DFS that checks for cycle or if already looked at
      def dfs(node):
        if node in visit: # already analyzed or currently visiting?
          return visit[node]
        visit[node] = True # mark as currently visiting
        for nei in adj[node]:
          if dfs(nei): # Returned true, means a cycle bc we are currently visiting it
            return True
        visit[node] = False # Mark as analyzed but not in current cycle

# STEP 3: Run DFS on all possible nodes
      for crs in range(numCourses):
        if dfs(crs):
          return False
      return True

print(solution(4, [[1,0],[2,0],[3,1],[3,2]]))