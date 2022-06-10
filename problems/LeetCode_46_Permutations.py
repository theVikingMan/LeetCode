import collections

def permute(nums):
    subset = []
    res = []
    values = collections.defaultdict(int)

    for n in nums:
        values[n] += 1

    def dfs():
        if len(subset) == len(nums):
            res.append(subset[::])
            return

        for key in values:
            if values[key] > 0:
                subset.append(key)
                values[key] -= 1
                dfs()

                subset.pop()
                values[key] += 1
    dfs()
    return res


print(permute([1, 2, 3]))