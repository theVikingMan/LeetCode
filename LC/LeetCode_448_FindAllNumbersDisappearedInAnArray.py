
def solution(nums):
    hash_table = {}
    result = []

    for num in nums:
        hash_table[num] = 1

    for num in range(1, len(nums) + 1):
        if num not in hash_table:
            result.append(num)

    return result


print(solution([4, 3, 2, 7, 8, 2, 3, 1]))
print(solution([1, 1, 1, 2, 3]))
print(solution([2, 2, 3, 1]))
