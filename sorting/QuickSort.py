
# T: worst case: O(n^2); best case: O(nlog(n)); average: O(nlog(n))
# S: O(log(n)) -> implemented recursively, n is size of call stack

def quickSort(array):
  quickSortHelper(array, 0, len(array) - 1)
  return array

def quickSortHelper(array, startIdx, endIdx):
  if startIdx >= endIdx: # have an array of size 1
    return
  pivotIdx = startIdx
  leftIdx, rightIdx = startIdx + 1, endIdx
  while rightIdx >= leftIdx:
    # if each pointer element is in its wrong place, swap
    if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
      swap(leftIdx, rightIdx, array)
    if array[leftIdx] <= array[pivotIdx]:
      leftIdx += 1
    if array[rightIdx] >= array[pivotIdx]:
      rightIdx -= 1
  swap(pivotIdx, rightIdx, array)
  leftIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
  if leftIsSmaller:
    quickSortHelper(array, startIdx, rightIdx - 1)
    quickSortHelper(array, rightIdx + 1, endIdx)
  else:
    quickSortHelper(array, rightIdx + 1, endIdx)
    quickSortHelper(array, startIdx, rightIdx - 1)
  return array

def swap(i, j, array):
  array[i], array[j] = array[j], array[i]

print(quickSort([1,4,2,7,5,4,2,9,1]))