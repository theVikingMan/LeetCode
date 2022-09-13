def solution(nums1, nums2):
  A, B = nums1, nums2
  total = len(A) + len(B)
  half = total // 2 # tells us how many elements in the left partition
  # only need to run BS on one of the arrays
  if len(B) < len(A): # make sure A is always the smaller in lengths of the two
    A, B = B, A

  l, r = 0, len(A) - 1

  while True:
    i = (l + r) // 2 # idx (-1 for idxs remember) pointer for A
    j = half - i - 2 # idx (-1 for idxs remember) pointer for B

    # conditionals are for
    Aleft = A[i] if i >= 0 else float('-inf') #
    Aright = A[i+1] if i + 1 < len(A) else float('inf')
    Bleft = B[j] if j >= 0 else float('-inf') #
    Bright = B[j+1] if j + 1 < len(B) else float('inf')

    # partition is correct
    if Aleft <= Bright and Bleft <= Aright:
      # odd total of elements
      if total % 2:
        return min(Aright, Bright)
      return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
    elif Aleft > Bright:
      r = i - 1
    else:
      l = i + 1

print(solution([1,1,5,6], [2,2,4]))

# T: O(min(n, m))
# S: O(1)  -> just using pointers

# Main Idea: Use BS to create two partitioned sub arrays that are the left partition
  # meaning the middle value is just next door but you have to adjust pointers to find
  # the partitions of each array that make up the left half of a theoritcal merged
  # array