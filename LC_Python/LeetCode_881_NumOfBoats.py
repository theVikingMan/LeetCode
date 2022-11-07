def numRescueBoats(people, limit):
    people.sort()
    l, r = 0, len(people) - 1
    result = 0

    while l <= r:
        currSum = people[l] + people[r]
        if currSum <= limit:
            l += 1
        r -= 1
        result += 1
    return result

print(numRescueBoats([1,2], 3)) # Output: 1
print(numRescueBoats([2,1,3], 3)) # Output: 2
print(numRescueBoats([1,3,3,4,5], 5)) # Output: 4