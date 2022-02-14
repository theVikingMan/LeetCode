def decompressRLElist(nums):
    ans = []
    slow = 0
    fast = 1
    while slow < (len(nums) - 1):
        temp = [nums[fast]] * nums[slow]
        ans = ans + temp
        slow += 2
        fast += 2
    return ans

print(decompressRLElist([1,2,3,4]))

# Another way with less memory
def decompressRLElist(nums):
        a=[]
        for i in range(1,len(nums),2):
            a+=[nums[i]]*nums[i-1]
        return(a)