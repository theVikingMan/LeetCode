
def lastRemaining(n):
  left = True
  step = head = 1
  remain = n

  while remain > 1:
    if left or remain % 2:
      head += step

    left = not left
    step *= 2
    remain = remain // 2

  return head

print(lastRemaining(12))


# def lastRemaining(n):
#   def helper(num, left):
#     if num == 1:
#       return 1

#     if left:
#       return 2 * helper(num // 2, 0)
#     elif num % 2:
#       return 2 * helper(num // 2, 1)
#     else:
#       return 2 * helper(num // 2, 1) - 1

#   return helper(n, 1)

# print(lastRemaining(10))


    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # [2, 4, 6, 8, 10]
    # [4, 8]
    # [8]