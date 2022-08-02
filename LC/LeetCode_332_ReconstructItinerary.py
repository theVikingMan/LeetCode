import collections

def findItinerary(tickets):
  graph = { start: collections.deque() for start, end in tickets } # deque so we can popleft vs list
  tickets.sort()

  for start, finish in tickets:
    graph[start].append(finish)

  res = ["JFK"]

  def dfs(curr):
    if len(res) == len(tickets) + 1:
      return True
    if curr not in graph: # Will trigger if a leaf node but not the end of the result
      return False

    temp = list(graph[curr])
    for nei in temp:
      res.append(nei)
      graph[curr].popleft()
      if dfs(nei):
        return res
      res.pop() # Need to perform back tracking incase of invalid plan
                # so then we need to try a different ordering that might be valid
                # but not necessarily in lexi order like the below
      graph[curr].append(nei)
    return False

  return dfs("JFK")

print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))