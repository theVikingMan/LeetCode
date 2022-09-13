# -------------- Heap (valid) --------- #

import heapq

def jobScheduling(startTime, endTime, profit):
    jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))], key=lambda x: x[0])
    heap = []
    currentProfit = 0
    maxProfit = 0
    for start, end, profit in jobs:
        # Calculate the total profit of all the jobs that would have end by this time(start: startTime of current job)
        while heap and heap[0][0] <= start:
            _, tempProfit = heapq.heappop(heap)
            currentProfit = max(currentProfit, tempProfit)

        # Push the job into heap to use it further. It's profit would be definitely currentProfit + profit(of current job)
        heapq.heappush(heap, (end, currentProfit + profit))
        maxProfit = max(maxProfit, currentProfit + profit)

    return maxProfit

print(jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))

# -------------- Recursion w/ memoization (too slow) --------- #

# def jobScheduling(startTime, endTime, profit):
#   data = [(start, end, p) for (start, end, p) in zip(startTime, endTime, profit)]
#   data.sort(key=lambda i:i[0])
#   dp = {}

#   def helper(i, e):
#     if i == len(data):
#       return 0
#     if (i, e) in dp:
#       return dp[(i, e)]

#     outcome = 0
#     for j in range(i, len(data)):
#       if data[j][0] >= e:
#         outcome = max(outcome, data[j][2] + helper(j+1, data[j][1]))
#     dp[(i, e)] = outcome
#     return dp[(i, e)]
#   return helper(0, -1)