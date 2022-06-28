import heapq

# ------------- HEAP APPROACH ------------ #

# def solution(array):
#   res = []
#   minH = []
#   for i, arr in enumerate(array):
#     heapq.heappush(minH, [arr[0], i, 0])
#   while minH:
#     val, arrIdx, idx = heapq.heappop(minH)
#     res.append(val)
#     if idx + 1 < len(array[arrIdx]):
#       heapq.heappush(minH, [array[arrIdx][idx+1], arrIdx, idx+1])
#   return res

# ------------- 2-Pointer Comparision APPROACH ------------ #

def solution(arr):
  if len(arr) < 2:
    return arr

  while len(arr) > 1:
    temp = []
    for i in range(0, len(arr), 2):
      one = arr[i]
      two = arr[i+1] if i+1 < len(arr) else []
      temp.append(mergeTwoArrs(one, two))
    arr = temp

  return arr

def mergeTwoArrs(arr1, arr2):
  res = []
  l, r = 0, 0
  while l < len(arr1) and r < len(arr2):
    if arr1[l] < arr2[r]:
      res.append(arr1[l])
      l += 1
    else:
      res.append(arr2[r])
      r += 1

  if l < len(arr1):
    res += arr1[l:]
  elif r < len(arr2):
    res += arr2[r:]

  return res


print(solution([[1,3,5,5,9], [0], [10,11], [2,3,4,5], [6,6,7]]))