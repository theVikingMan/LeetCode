# Memoization solution

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


print(fib(50))

# Base recursive function

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)


# print(fib(10))
