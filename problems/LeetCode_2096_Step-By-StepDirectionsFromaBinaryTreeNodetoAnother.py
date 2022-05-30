import collections

def getDirections(root, startValue, destValue):
  # transform tree into a UNDIRECTED graph
  graph = collections.defaultdict(list)
  queue = collections.deque([root])

  # in-order traversal
  while queue:
    node = queue.popleft()
    if node.left:
      graph[node.left.val].append((node.val, 'U')) # connect left child to parent
      graph[node.val].append((node.left.val, 'L')) # connect parent to left child
      queue.append(node.left)
    if node.right:
      graph[node.right.val].append((node.val, 'U')) # connect right child to parent
      graph[node.val].append((node.right.val, 'R')) # connect parent to right child
      queue.append(node.right)

  # BFS over created graph until target is found
  queue = collections.deque([(startValue, '')])
  seen = set()

  # attempted recursive BFS but too much memory
  while queue:
    node, direction = queue.popleft()
    if node in seen:
      continue
    if node == destValue:
      return direction
    seen.add(node)
    for nei, d in graph[node]:
      if nei not in seen:
        queue.append((nei, direction + d))
