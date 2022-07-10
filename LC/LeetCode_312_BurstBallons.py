def maxCoins(nums):
    cache = {}
    nums = [1] + nums + [1]

    for offset in range(2, len(nums)):
        for left in range(len(nums) - offset):
            right = left + offset
            for pivot in range(left + 1, right):
                coins = nums[left] * nums[pivot] * nums[right]
                coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)
                cache[(left, right)] = max(coins, cache.get((left, right), 0))
    return cache.get((0, len(nums) - 1), 0)


def maxCoins(nums):
    dp = {}
    nums = [1] + nums + [1]

    def helper(l, r):
      if l > r:
        return 0
      if (l, r) in dp:
        return dp[(l, r)]

      dp[(l, r)] = 0
      for i in range(l, r+1):
        coins = nums[l-1] * nums[i] * nums[r+1]
        left, right = helper(l, i-1), helper(i+1, r)
        coins = coins + left + right
        dp[(l, r)] = max(dp[(l, r)], coins)

      return dp[(l, r)]

    return helper(1, len(nums) - 2)

# ------------- Recursion w/ Memoization (too slow) ----------- #

def maxCoins(nums):
  dp = {}

  def helper(arr):
    if len(arr) == 0:
      return 0
    if tuple(arr) in dp:
      return dp[tuple(arr)]

    outcome = 0
    for i in range(len(arr)):
      l = arr[i-1] if i-1 >= 0 else 1
      r = arr[i+1] if i+1 < len(arr) else 1
      product = l * arr[i] * r
      newArr = arr[:i] + arr[i+1:]
      outcome = max(outcome, product + helper(newArr))
    dp[tuple(arr)] = outcome
    return dp[tuple(arr)]

  return helper(nums)

