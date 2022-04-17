def climbStairs(n):
    after, before = 1, 0

    for i in range(n):
        temp = after + before
        before = after
        after = temp
    return after

print(climbStairs(4))

