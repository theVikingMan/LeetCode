def canVisitAllRooms(rooms):
  roomLength = len(rooms)
  adj = {i:[] for i in range(roomLength)}
  for i in range(roomLength):
    for key in rooms[i]:
      adj[i].append(key)

  visit = set()

  def dfs(curr):
    if curr in visit:
      return
    visit.add(curr)
    for nei in adj[curr]:
      dfs(nei)
    return True

  return dfs(0) and len(visit) == roomLength

print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))