# ---------- Optimized way --------- #

def numberOfWays(s):
  dp = {"0": 0, "1": 0, "01": 0, "10": 0, "010": 0, "101": 0}
  for num in s:
    if num == "0":
      dp["0"] += 1
      dp["10"] += dp["1"]
      dp["010"] += dp["01"]
    else:
      dp["1"] += 1
      dp["01"] += dp["0"]
      dp["101"] += dp["10"]
  return dp["101"] + dp["010"]

print(numberOfWays("001101"))

# ---------- Memoized (TOO SLOW) ----------- #

def numberOfWays(s):
  cache = {}

  def dfs(i, prev, arr):
    aLen = len(arr)
    if aLen == 3:
      return 1
    if i == len(s):
      return 0
    if (i, aLen, prev) in cache:
      return cache[(i, aLen, prev)]

    outcome = 0
    if s[i] != prev:
      outcome += dfs(i+1, s[i], arr + [s[i]])
    outcome += dfs(i+1, prev, arr)
    cache[((i, aLen, prev))] = outcome
    return cache[((i, aLen, prev))]

  return dfs(0, -1, [])

print(numberOfWays("001101"))