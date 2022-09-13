import collections

def killProcess(pid, ppid, kill):
  graph = collections.defaultdict(list)
  for child, par in zip(pid, ppid):
    graph[par].append(child)

  q = collections.deque([kill])
  res = []

  while q:
    toKill = q.popleft()
    res.append(toKill)

    if toKill in graph:
      q.extend(graph[toKill])

  return res

print(killProcess([1,3,10,5], [3,0,5,3]))