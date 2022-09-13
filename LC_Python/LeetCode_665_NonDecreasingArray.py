def checkPossibility(N):
  err = 0
  for i in range(1, len(N)):
      if N[i] < N[i-1]:
          if err or (i > 1 and i < len(N) - 1 and N[i-2] > N[i] and N[i+1] < N[i-1]):
              return False
          err = 1
  return True

print(checkPossibility([1, 4, 3, 4]))

# https://leetcode.com/problems/non-decreasing-array/discuss/?currentPage=1&orderBy=most_votes&query=