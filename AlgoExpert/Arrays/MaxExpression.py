# -------------- DP ------------ #

def maximizeExpression(array):
    if len(array) < 4:
        return 0

    step1 = [array[0]]
    step2 = [float('-inf')]
    step3 = [float('-inf') for _ in range(2)]
    step4 = [float('-inf') for _ in range(3)]

    for i in range(1, len(array)):
        currMax = max(step1[i-1], array[i])
        step1.append(currMax)

    for i in range(1, len(array)):
        currMax = max(step2[i-1], step1[i-1] - array[i])
        step2.append(currMax)

    for i in range(2, len(array)):
        currMax = max(step3[i-1], step2[i-1] + array[i])
        step3.append(currMax)

    for i in range(3, len(array)):
        currMax = max(step4[i-1], step3[i-1] - array[i])
        step4.append(currMax)
    return step4[-1]

# -------------- Memoized Recursion ------------ #

def maximizeExpression(array):
    if len(array) < 4:
        return 0

    dp = {}
    def helper(i, curr, prev):
        if i == 0:
            return curr
        if (i, curr) in dp:
            return dp[(i, curr)]
        temp = float('-inf')
        for j in range(prev+1, len(array) - i + 1):
            if i % 2:
                temp = max(temp, helper(i-1, curr - array[j], j))
            else:
                temp = max(temp, helper(i-1, curr + array[j], j))
        dp[(i, curr)] = temp
        return dp[(i, curr)]

    return helper(4, 0, -1)

# -------------- Recursion ------------ #

# def maximizeExpression(array):
#     if len(array) < 4:
#         return 0

#     def helper(i, curr, prev):
#         if i == 0:
#             return curr
#         temp = float('-inf')
#         for j in range(prev+1, len(array) - i + 1):
#             if i % 2:
#                 temp = max(temp, helper(i-1, curr - array[j], j))
#             else:
#                 temp = max(temp, helper(i-1, curr + array[j], j))
#         return temp

#     return helper(4, 0, -1)

print(maximizeExpression([3, 6, 1, -3, 2, 7]))