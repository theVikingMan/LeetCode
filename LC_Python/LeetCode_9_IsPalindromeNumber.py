def isPalindrome(x):
    res = 0
    remain = x
    def mode(x, m):
        if x >= 0:
            return x % m
        return x % -m

    if x < 0:
        return False
    while remain:
        res = res * 10 + (mode(remain, 10))
        remain = remain // 10.0
    return res == x

print(isPalindrome(121))