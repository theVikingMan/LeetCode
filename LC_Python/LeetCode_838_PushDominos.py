import collections

def pushDominoes(dominoes):
  doms = list(dominoes)
  queue = collections.deque()

  for i, d in enumerate(doms):
    if d != ".": queue.append((i, d))

  while queue:
    i, d = queue.popleft()

    if d == "L"and i > 0 and doms[i - 1] == ".":
        doms[i - 1] = "L"
        queue.append((i - 1, "L"))
    elif d == "R": # right leaning domino
        if i + 1 < len(doms) and doms[i + 1] == ".":
          if i + 2 < len(doms) and doms[i + 2] == "L":
            queue.popleft()
          else:
            doms[i + 1] = "R"
            queue.append((i + 1, "R"))

  return "".join(doms)

print(pushDominoes(".L.R...LR..L.."))