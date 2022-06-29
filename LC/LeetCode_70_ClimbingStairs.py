def climbStairs(n):
    after, before = 1, 0

    for _ in range(n):
        temp = after + before
        before = after
        after = temp
    return after

print(climbStairs(4))

# ---------- Top down DP ---------- #

# def climbStairs(n):
#   dp = {1:1,
#         2:2}
#   def recurse(num):
#     if num in dp:
#       return dp[num]
#     dp[num] = recurse(num-1) + recurse(num-2)
#     return dp[num]
#   recurse(n)
#   return dp[n]

