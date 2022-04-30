def validMountainArray(arr):
    next = 1
    curr = 0
    up_move = False
    down_move = False
    while next < len(arr):
        if arr[next] - arr[curr] > 0 and down_move is False:
            next += 1
            curr += 1
            up_move = True
        elif arr[next] - arr[curr] < 0 and up_move is True:
            next += 1
            curr += 1
            down_move = True
        else:
            return False
    return up_move and down_move


# def validMountainArray(A):
#     N = len(A)
#     i = 0
#     # walk up
#     while i+1 < N and A[i] < A[i+1]:
#         i += 1
#     # peak can't be first or last
#     if i == 0 or i == N-1:
#         return False
#     # walk down
#     while i+1 < N and A[i] > A[i+1]:
#         i += 1
#     return i == N-1

print(validMountainArray([1, 2]))
print(validMountainArray([3, 5, 5]))
print(validMountainArray([0, 3, 2, 1]))
