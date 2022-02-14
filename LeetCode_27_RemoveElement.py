#CORRECT way to both have the k output and the right ordering without
#dublicating
def removeElement(nums, val):
    start, end = 0, len(nums) - 1
    while start <= end:
        if nums[start] == val:
            nums[start], nums[end], end = nums[end], nums[start], end - 1
        else:
            start +=1
    return nums

print(removeElement([0,1,2,2,3,0,4,2], 2))

'''
#To note, they reutrn the wrong list as the last nums that isnt equal
#to val is dublicated. The function just replaces / dubs the none
#vale number

#Solving it the LeetCode way
def removeElement(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        else:
            nums.append(nums[i])
            del nums[nums.index(nums[i])]
    return nums

print(removeElement([0,1,2,2,3,0,4,2], 2))


#Solving using a dictionary
def removeElement(nums, val):
    dict1={}
    i=0
    for index,val1 in enumerate(nums):
        if(val1!=val):
            dict1[i]=val1
            i += 1
    for key,value in dict1.items():
        nums[key]=value
    print(nums)
    return(len(dict1.keys()))
removeElement([0,1,2,2,3,0,4,2], 2)
'''
