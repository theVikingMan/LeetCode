def permuteUnique(nums):
    result = []
    subset = []
    mapping = {}
    for num in nums:
        mapping[num] = 1 + mapping.get(num, 0)

    def dfs():
        if len(subset) == len(nums):
            result.append(subset[::])
            return
        # Hash map helps fill back up the reserves of the other nums
        # and since we loop over the keys, we wont have the same starting
        # num again once we have returned all perms for that key
        for key in mapping:
            if mapping[key] > 0:
                subset.append(key)
                mapping[key] -= 1
                dfs()

                subset.pop()
                mapping[key] += 1

    dfs()
    return result


print(permuteUnique([1, 1, 2]))