def combine(n, k):
    result = []

    def dfs(start, comb):
        if len(comb) == k:
            result.append(comb[::])
            return

        for i in range(start, n+1):
            comb.append(i)
            dfs(i+1, comb)
            comb.pop()

    dfs(1, [])
    return result

print(combine(4, 2))