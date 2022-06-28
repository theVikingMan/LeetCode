def bubbleSort(array):
  if len(array) < 2:
    return array
  end = len(array) - 1
  isSorted = True # optimization: if no sorting occured, break. Kills unneed iterations
  while end > 0 and isSorted:
    isSorted = False
    for i in range(end):
        if array[i] > array[i+1]:
          array[i], array[i+1] = array[i+1], array[i]
          isSorted = True
    end -= 1 # optimization: Every iteration brings largest num to the end
  return array

print(bubbleSort([1, 2, 3, 4]))
print(bubbleSort([8, 3, 4, 1, 5]))

# T: O(n^2)
# S: O(1)