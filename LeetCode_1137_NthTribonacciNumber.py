# def tri_fib(n):
#     lst = [0, 1, 1]
#     if n < 2:
#         return lst[n]
#     else:            
#         for i in range(n-2):
#             lst.append(sum(lst))
#             lst.pop(0)
#     return lst.pop()

def tri_fib(n):
    if n < 3:
        return 1 if n else 0
    a, b, c = 0, 1, 1
    for i in range(n-2):
        a, b, c = b, c, a + b + c
    return c


print(tri_fib(10))