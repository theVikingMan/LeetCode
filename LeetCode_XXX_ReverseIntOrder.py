def descending_order(num):
    ans = 0
    c = num
    while c != 0:
        ans = ans * 10 + c % 10
        c = c // 10
    return ans


print(descending_order(42145))
