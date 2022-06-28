# -------------- Good approach (not best memory) ----------- #

def mergeSort(array):
  if len(array) == 1:
    return array
  m = len(array) // 2
  left = mergeSort(array[:m])
  right = mergeSort(array[m:])
  return mergeSortedArrays(left,right)

def mergeSortedArrays(leftArr, rightArr):
  output = []
  l, r = 0, 0
  while l < len(leftArr) and r < len(rightArr):
    if leftArr[l] < rightArr[r]:
      output.append(leftArr[l])
      l += 1
    else:
      output.append(rightArr[r])
      r += 1

  if l < len(leftArr):
    output += leftArr[l:]
  elif r < len(rightArr):
    output += rightArr[r:]

  return output

print(mergeSort([1,4,2,7,5,4,2,9,1]))

# T: O(nlog(n))
# S: O(n) - optimized approach

# Divid & Conquer approach
# STEP 1: Recurse by dividing in half (l + r // 2)
    # the arrays until base case of array
    # containing only one element
    # T: O(log(n))
# STEP 2: Merge using 2 pointers and comparing smallest elements
    # and adding to output array then returning that sorted array
    # upwards until whole array is put together
    # T: O(n)