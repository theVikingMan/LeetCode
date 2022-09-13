from itertools import accumulate

def totalStrength(A):
    res, ac, mod, stack, acc = 0, 0, 10 ** 9 + 7, [-1], [0]
    A += [0]
    for r, a in enumerate(A):
        ac += a
        acc.append(ac + acc[-1])
        while stack and A[stack[-1]] > a:
            i = stack.pop()
            l = stack[-1]
            lacc = acc[i] - acc[max(l, 0)]
            racc = acc[r] - acc[i]
            ln, rn = i - l, r - i
            res += A[i] * (racc * ln - lacc * rn) % mod
        stack.append(r)
    return res % mod

print(totalStrength([1, 3, 1, 2]))