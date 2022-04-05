def containsDuplicates(nums):
  mapping = {}
  for i in nums:
      if i not in mapping:
          mapping[i] = 1
      elif i in mapping:
          return True
      else:
          return False

print(containsDuplicates([1,1,1,3,3,4,3,2,4,2]))