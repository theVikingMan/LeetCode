def solution(n):
    c = 0
    while n:
        n &= n-1
        c += 1
    return c


print(solution(3))
