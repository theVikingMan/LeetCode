def myPow(x, n):
  def helper(x, n):
    if x == 0: return 0
    if n == 0: return 1

    res = helper(x, n // 2)
    res = res * res
    return res * x if n % 2 else res # mod by 2 to see if we need another multi (3^5 = [3^2 * 3^2] * 3)

  output = helper(x, abs(n))
  return output if n >= 0 else 1 / output

print(myPow(3, 5))

# ------------- Brute Force (times out) ------------- #

# def solution(x, n):
#   res = x
#   if n == 0:
#     return 1
#   for _ in range(abs(n) -1):
#     res *= x

#   return res if n > 0 else 1 / res


# ------------ Simple (passes) ------------ #

# def solution(x, n):
#   return x ** n