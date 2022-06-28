def selectionSort(arr):
  for i in range(len(arr)):
    curMinIdx = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[curMinIdx]:
        curMinIdx = j
    arr[i], arr[curMinIdx] = arr[curMinIdx], arr[i]
  return arr

print(selectionSort([5,1,3,6]))

# T: O(n^2)
# S: O(1)