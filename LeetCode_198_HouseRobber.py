def rob(nums):
    # base cases
    # think about the game state starting 2 plays back for rob2 and
    # 1 play back state for rob1
    rob1, rob2 = 0, 0

    for n in nums:
        # Rob1: [0, 1, 2, 4]
        # Rob2: [1, 2, 4, 4]
        # Track max state up to that point but also tracks
        # robbing every other house
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp
    return max(rob1, rob2)

print(rob([1, 2, 3, 1]))