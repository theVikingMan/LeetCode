def combinationSum(candidates, target):
  res = []

  def dfs(i, curr, total):
    # Base case: we have found a target set
    if total == target:
      res.append(curr.copy())
      return

    # Base case: we have added to many numbers or we have gone over
    if i >= len(candidates) or total > target:
      return

    # Decision 1: include so add it to the temp total
    curr.append(candidates[i])
    dfs(i, curr, total + candidates[i])

    # Decision 2: Dont include so the total is the same and move to the next
    # num to make a deicision on
    curr.pop()
    dfs(i + 1, curr, total)

  dfs(0, [], 0)
  return res

print(combinationSum([2,3,6,7], 7))