# def climbStairs(n):
#     a = 1
#     b = 1
#     for _ in range(n):
#         (a, b) = (b, a + b)
#     return a

# print(climbStairs(7))


# Recursivly with memoization
# def climbStairs(n):
#     def dp(i):
#         if i <= 2:
#             return i
#         if i not in memo:
#             memo[i] = dp(i - 1) + dp(i - 2)
#         return memo[i]

#     memo = {}
#     return dp(n)

# print(climbStairs(7))


# Bottoms-up with iteration
def climbStairs(n):
    if n < 2:
        return n

    # An array that represents the answer to the problem for a given state
    dp = [0] * (n + 1)
    dp[1] = 1  # Base cases
    dp[2] = 2  # Base cases

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # Recurrence relation

    return dp[n]


print(climbStairs(7))
